"""
utils.py - Funciones de cálculo (distancia, conversiones y tiempos).

No usa input() ni print() (salvo en el bloque de prueba al final).
"""

from math import radians, sin, cos, asin, sqrt

RADIO_TIERRA_KM = 6371      # radio medio de la Tierra
KM_A_MILLAS = 0.621371      # 1 km = 0.621371 millas


def calcular_distancia(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia en línea recta (en km) entre dos puntos
    usando la fórmula de Haversine.

    Parámetros: latitud y longitud de cada punto, en grados.
    Devuelve: distancia en kilómetros (float).
    """
    # La fórmula necesita los ángulos en radianes
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    # min(1, ...) evita un error de redondeo en puntos casi opuestos
    return 2 * RADIO_TIERRA_KM * asin(min(1, sqrt(a)))


def km_a_millas(km):
    """Convierte kilómetros a millas."""
    return km * KM_A_MILLAS


def calcular_tiempo(distancia_km, velocidad_kmh):
    """Devuelve el tiempo en horas decimales: tiempo = distancia / velocidad."""
    return distancia_km / velocidad_kmh


def formatear_tiempo(horas):
    """
    Convierte horas decimales a texto 'X h Y min'.

    Ejemplo: 3.5 -> '3 h 30 min'
    """
    total_minutos = round(horas * 60)       # redondeamos primero a minutos enteros
    h, m = divmod(total_minutos, 60)        # así nunca aparece '60 min'
    return f"{h} h {m:02d} min"


# Pruebas rápidas: solo se ejecutan al correr utils.py directamente
if __name__ == "__main__":
    # Madrid -> París: debe dar aproximadamente 1,053 km
    d = calcular_distancia(40.4168, -3.7038, 48.8566, 2.3522)
    print(f"Madrid-París: {d:,.2f} km ({km_a_millas(d):,.2f} millas)")
    print(f"Mismo punto: {calcular_distancia(10, 10, 10, 10)} km")
    print(formatear_tiempo(3.5))    # 3 h 30 min
    print(formatear_tiempo(0))      # 0 h 00 min