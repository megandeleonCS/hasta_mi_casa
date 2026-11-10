"""
ui.py - Command-line interface functions for user interaction.
"""


def mostrar_menu():
    """Displays main navigation menu."""
    print("\n=== Calculadora de Distancias ===")
    print("1. Calcular distancia")
    print("2. Salir")


def pedir_texto(mensaje):
    """Prompts input until non-empty string is provided."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Este campo no puede estar vacío. Intenta de nuevo.")


def pedir_ciudad(tipo):
    """Prompts for city name ('origen' or 'destino')."""
    return pedir_texto(f"Ciudad de {tipo}: ")


def pedir_pais(tipo):
    """Prompts for country name ('origen' or 'destino')."""
    return pedir_texto(f"País de {tipo}: ")


def pedir_unidad():
    """Prompts user to select distance unit (km or mi)."""
    while True:
        unidad = input("Unidad de distancia (km/mi): ").strip().lower()
        if unidad in ["km", "mi"]:
            return unidad
        print("Unidad no válida. Escribe 'km' para kilómetros o 'mi' para millas.")


def mostrar_resumen(ciudad_o, pais_o, ciudad_d, pais_d, unidad):
    """Prints input confirmation summary."""
    nombre_unidad = "kilómetros" if unidad == "km" else "millas"
    print("\n--- Resumen ---")
    print(f"Origen:  {ciudad_o}, {pais_o}")
    print(f"Destino: {ciudad_d}, {pais_d}")
    print(f"Unidad:  {nombre_unidad}")


def mostrar_coordenadas(etiqueta, datos):
    """Displays formatted coordinate result."""
    print(
        f"{etiqueta} {datos['nombre']}, {datos['pais']} "
        f"→ lat {datos['lat']}, lon {datos['lon']}"
    )