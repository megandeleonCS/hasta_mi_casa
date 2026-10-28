"""
main.py - Calculadora de Distancias (Pasos 4 y 5)

Este archivo maneja la interacción con el usuario: menú, preguntas
y formato de las respuestas. La consulta a la API vive en api.py.
Todavía no se calcula ninguna distancia (eso se hace en M12).
"""

import sys

from api import obtener_coordenadas

# Evita caracteres raros (�) con acentos en la consola de Windows
sys.stdout.reconfigure(encoding="utf-8")


def mostrar_menu():
    """Muestra el menú principal."""
    print("\n=== Calculadora de Distancias ===")
    print("1. Calcular distancia")
    print("2. Salir")


def pedir_texto(mensaje):
    """
    Pide un texto con input() y vuelve a preguntar mientras el usuario
    deje el campo vacío o escriba solo espacios.
    Devuelve el texto sin espacios al inicio ni al final.
    """
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Este campo no puede estar vacío. Intenta de nuevo.")


def pedir_ciudad(tipo):
    """Pide una ciudad. 'tipo' es 'origen' o 'destino' (para el mensaje)."""
    return pedir_texto(f"Ciudad de {tipo}: ")


def pedir_pais(tipo):
    """Pide un país. 'tipo' es 'origen' o 'destino' (para el mensaje)."""
    return pedir_texto(f"País de {tipo}: ")


def pedir_unidad():
    """
    Pregunta la unidad preferida y rechaza respuestas inválidas.
    Devuelve 'km' o 'millas'.
    """
    while True:
        unidad = input("Unidad (km/millas): ").strip().lower()
        if unidad in ("km", "millas"):
            return unidad
        print("Unidad no válida. Escribe 'km' o 'millas'.")


def mostrar_resumen(ciudad_o, pais_o, ciudad_d, pais_d, unidad):
    """Imprime el resumen de confirmación antes de consultar los datos."""
    nombre_unidad = "kilómetros" if unidad == "km" else "millas"
    print("\n--- Resumen ---")
    print(f"Origen:  {ciudad_o}, {pais_o}")
    print(f"Destino: {ciudad_d}, {pais_d}")
    print(f"Unidad:  {nombre_unidad}")


def consultar_lugar(tipo, ciudad, pais):
    """
    Consulta las coordenadas de un lugar. Si falla, vuelve a pedir SOLO
    ese lugar (ciudad y país) hasta que la API lo encuentre.
    Devuelve el diccionario con nombre, pais, lat y lon.
    """
    while True:
        datos = obtener_coordenadas(ciudad, pais)
        if datos is not None:
            return datos
        print(f"No se encontró '{ciudad}, {pais}' o hubo un problema de conexión.")
        ciudad = pedir_ciudad(tipo)
        pais = pedir_pais(tipo)


def mostrar_coordenadas(etiqueta, datos):
    """Imprime las coordenadas de un lugar con formato."""
    print(
        f"{etiqueta} {datos['nombre']}, {datos['pais']} "
        f"→ lat {datos['lat']}, lon {datos['lon']}"
    )


def calcular_distancia():
    """Flujo completo de la opción 1: preguntas, resumen y consulta."""
    # Paso 4: entradas del usuario
    ciudad_o = pedir_ciudad("origen")
    pais_o = pedir_pais("origen")
    ciudad_d = pedir_ciudad("destino")
    pais_d = pedir_pais("destino")
    unidad = pedir_unidad()

    mostrar_resumen(ciudad_o, pais_o, ciudad_d, pais_d, unidad)

    # Paso 5: consulta a la API
    print("Consultando datos...")
    origen = consultar_lugar("origen", ciudad_o, pais_o)
    destino = consultar_lugar("destino", ciudad_d, pais_d)

    mostrar_coordenadas("Origen: ", origen)
    mostrar_coordenadas("Destino:", destino)
    # En M12 aquí se calculará la distancia entre origen y destino


def main():
    """Ciclo principal: repite el menú hasta que el usuario elija salir."""
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


# Solo se ejecuta al correr main.py directamente
if __name__ == "__main__":
    main()