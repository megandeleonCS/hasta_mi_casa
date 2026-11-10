"""
cache.py - Handles persistence for cached coordinate data.
"""

import json
import os

#CACHE_FILE = "M11_con_modular_programming/coordenadas_cache.json"

# Define the subfolder and file path
CACHE_DIR = "data"
CACHE_FILE = os.path.join(CACHE_DIR, "coordenadas_cache.json")


def cargar_cache():
    """Reads local JSON cache file if present; returns an empty dict on error."""
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def guardar_cache(cache):
    """Saves updated dictionary cache to the local JSON file inside the subfolder."""
    try:
        # Create the subfolder automatically if it doesn't exist
        os.makedirs(CACHE_DIR, exist_ok=True)

        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"[CACHE ERROR] Could not save file: {e}")