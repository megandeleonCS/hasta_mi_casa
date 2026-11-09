"""
api.py - Open-Meteo API connection with JSON caching layer.
"""

import unicodedata

import requests
from cache import cargar_cache, guardar_cache

URL_GEOCODING = "https://geocoding-api.open-meteo.com/v1/search"


def normalizar(texto):
    """Strips accents, spaces, and lowers string for key comparison."""
    texto = unicodedata.normalize("NFD", texto.strip().lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def obtener_coordenadas(ciudad, pais):
    """
    Fetches coordinates for a location. Checks local JSON cache first;
    falls back to Open-Meteo API on cache miss.
    """
    clave_cache = f"{normalizar(ciudad)},{normalizar(pais)}"

    # 1. Check local cache
    cache = cargar_cache()
    if clave_cache in cache:
        return cache[clave_cache]

    # 2. Fetch from API if missing
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
    except (requests.exceptions.RequestException, ValueError):
        return None

    resultados = datos.get("results", [])
    pais_buscado = normalizar(pais)

    for lugar in resultados:
        if normalizar(lugar.get("country", "")) == pais_buscado:
            resultado = {
                "nombre": lugar.get("name"),
                "pais": lugar.get("country"),
                "lat": lugar.get("latitude"),
                "lon": lugar.get("longitude"),
            }
            # Save new coordinate to cache
            cache[clave_cache] = resultado
            guardar_cache(cache)
            return resultado

    return None