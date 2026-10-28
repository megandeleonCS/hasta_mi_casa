"""
api.py - Conexión con la API de Geocodificación de Open-Meteo.

Este módulo NO usa input() ni print() (salvo en el bloque de prueba al final).
Solo consulta la API y devuelve datos; main.py decide qué mostrar al usuario.
"""

import unicodedata

import requests

# Dirección base de la API (gratis, no requiere clave)
URL_GEOCODING = "https://geocoding-api.open-meteo.com/v1/search"


def normalizar(texto):
    """
    Prepara un texto para compararlo: minúsculas, sin espacios
    extra y sin acentos.

    Ejemplo: ' México ' -> 'mexico'
    """
    texto = unicodedata.normalize("NFD", texto.strip().lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def obtener_coordenadas(ciudad, pais):
    """
    Busca una ciudad en la API Open-Meteo y devuelve sus coordenadas.

    Parámetros:
        ciudad (str): nombre de la ciudad, por ejemplo "San Marcos".
        pais (str): país de la ciudad, por ejemplo "Guatemala".

    Devuelve:
        dict con las llaves "nombre", "pais", "lat" y "lon", o
        None si no hay coincidencia o si ocurre un error de conexión.
    """
    parametros = {
        "name": ciudad.strip(),  # la API busca solo el nombre del lugar
        "count": 10,             # pedimos varios resultados para filtrar por país
        "language": "es",        # nombres de países en español
        "format": "json",
    }

    try:
        respuesta = requests.get(URL_GEOCODING, params=parametros, timeout=10)
        respuesta.raise_for_status()  # error si el código HTTP no es 200
        datos = respuesta.json()      # convierte el JSON en diccionario de Python
    except requests.exceptions.Timeout:
        return None  # la API tardó demasiado en responder
    except requests.exceptions.RequestException:
        return None  # sin internet u otro error de red o HTTP
    except ValueError:
        return None  # la respuesta no era un JSON válido

    # Si la ciudad no existe, la API no incluye "results"
    resultados = datos.get("results", [])

    # Elegimos el primer resultado cuyo país coincida con el ingresado
    pais_buscado = normalizar(pais)
    for lugar in resultados:
        if normalizar(lugar.get("country", "")) == pais_buscado:
            return {
                "nombre": lugar.get("name"),
                "pais": lugar.get("country"),
                "lat": lugar.get("latitude"),
                "lon": lugar.get("longitude"),
            }

    return None  # ningún resultado coincidió con el país


# Este bloque solo se ejecuta al correr api.py directamente
# (no cuando main.py lo importa). Sirve para probar el módulo solo.
if __name__ == "__main__":
    import sys

    # Evita caracteres raros (�) con acentos en la consola de Windows
    sys.stdout.reconfigure(encoding="utf-8")

    print(obtener_coordenadas("Salt Lake City", "Estados Unidos"))
    print(obtener_coordenadas("San Marcos", "Guatemala"))
    print(obtener_coordenadas("Bogotá ", "colombia"))        # espacios y mayúsculas
    print(obtener_coordenadas("Ciudad Inventada", "Guatemala"))  # debe dar None