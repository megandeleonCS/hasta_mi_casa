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
        "name": ciudad.strip(),
        "count": 10,
        "language": "es",
        "format": "json",
    }

    try:
        respuesta = requests.get(URL_GEOCODING, params=parametros, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()
    except requests.exceptions.Timeout:
        return None
    except requests.exceptions.RequestException:
        return None
    except ValueError:
        return None

    resultados = datos.get("results", [])

    pais_buscado = normalizar(pais)
    for lugar in resultados:
        if normalizar(lugar.get("country", "")) == pais_buscado:
            return {
                "nombre": lugar.get("name"),
                "pais": lugar.get("country"),
                "lat": lugar.get("latitude"),
                "lon": lugar.get("longitude"),
            }

    return None


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")

    print(obtener_coordenadas("Salt Lake City", "Estados Unidos"))
    print(obtener_coordenadas("San Marcos", "Guatemala"))
    print(obtener_coordenadas("Bogotá ", "colombia"))
    print(obtener_coordenadas("Ciudad Inventada", "Guatemala"))