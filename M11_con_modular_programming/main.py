"""
main.py - Application entry point and controller flow.
"""

import sys

from api import obtener_coordenadas
from distancia import calcular_haversine
from ui import (
    mostrar_coordenadas,
    mostrar_menu,
    mostrar_resumen,
    pedir_ciudad,
    pedir_pais,
    pedir_unidad,
)

sys.stdout.reconfigure(encoding="utf-8")


def consultar_lugar(tipo, ciudad, pais):
    """Retries lookup via api.py until valid location is found."""
    while True:
        datos = obtener_coordenadas(ciudad, pais)
        if datos is not None:
            return datos
        print(f"No se encontró '{ciudad}, {pais}' o hubo un problema de conexión.")
        ciudad = pedir_ciudad(tipo)
        pais = pedir_pais(tipo)


def calcular_distancia():
    """Option 1 execution flow."""
    ciudad_o = pedir_ciudad("origen")
    pais_o = pedir_pais("origen")
    ciudad_d = pedir_ciudad("destino")
    pais_d = pedir_pais("destino")
    unidad = pedir_unidad()

    mostrar_resumen(ciudad_o, pais_o, ciudad_d, pais_d, unidad)

    print("\nConsultando datos...")
    origen = consultar_lugar("origen", ciudad_o, pais_o)
    destino = consultar_lugar("destino", ciudad_d, pais_d)

    mostrar_coordenadas("Origen: ", origen)
    mostrar_coordenadas("Destino:", destino)

    distancia = calcular_haversine(
        origen["lat"], origen["lon"], destino["lat"], destino["lon"], unidad
    )
    nombre_unidad = "kilómetros" if unidad == "km" else "millas"
    print(f"\nDistancia estimada: {distancia} {nombre_unidad}")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            calcular_distancia()
        elif opcion == "2":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Elige 1 o 2.")


if __name__ == "__main__":
    main()