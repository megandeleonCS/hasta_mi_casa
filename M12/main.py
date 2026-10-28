"""
main.py - Calculadora de Distancias (Paso 7: refactorizado con la clase Ciudad)

Menú en bucle -> pedir ciudades -> consultar la API -> calcular distancia
y tiempos -> mostrar un resumen. Las coordenadas vienen de api.py y los
cálculos de utils.py.
"""

import sys

from api import obtener_coordenadas
from utils import km_a_millas, calcular_tiempo, formatear_tiempo

# Evita caracteres raros (�) con acentos en la consola de Windows
sys.stdout.reconfigure(encoding="utf-8")

# Velocidades promedio (km/h)
# Avión: velocidad de crucero típica de un avión comercial (800-900 km/h).
VELOCIDAD_AVION = 800
# Auto: promedio realista en carretera, contando curvas, tráfico y paradas.
VELOCIDAD_AUTO = 80


# ---------- Entradas del usuario (Paso 4) ----------

def mostrar_menu():
    """Muestra el menú principal."""
    print("\n=== Calculadora de Distancias ===")
    print("1. Calcular distancia")
    print("2. Salir")


def pedir_texto(mensaje):
    """
    Pide un texto con input() y vuelve a preguntar mientras el usuario
    deje el campo vacío o escriba solo espacios.
    """
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Este campo no puede estar vacío. Intenta de nuevo.")


def pedir_ciudad(tipo):
    """Pide una ciudad. 'tipo' es 'origen' o 'destino'."""
    return pedir_texto(f"Ciudad de {tipo}: ")


def pedir_pais(tipo):
    """Pide un país. 'tipo' es 'origen' o 'destino'."""
    return pedir_texto(f"País de {tipo}: ")


def pedir_unidad():
    """Pregunta la unidad preferida. Devuelve 'km' o 'millas'."""
    while True:
        unidad = input("Unidad (km/millas): ").strip().lower()
        if unidad in ("km", "millas"):
            return unidad
        print("Unidad no válida. Escribe 'km' o 'millas'.")


def mostrar_resumen_entrada(ciudad_o, pais_o, ciudad_d, pais_d, unidad):
    """Imprime el resumen de confirmación antes de consultar los datos."""
    nombre_unidad = "kilómetros" if unidad == "km" else "millas"
    print("\n--- Resumen ---")
    print(f"Origen:  {ciudad_o}, {pais_o}")
    print(f"Destino: {ciudad_d}, {pais_d}")
    print(f"Unidad:  {nombre_unidad}")


# ---------- Consulta a la API (Paso 5) ----------

def consultar_lugar(ciudad, pais):
    """
    Consulta un lugar y muestra el mensaje adecuado si algo falla.
    Devuelve un objeto Ciudad o None si hubo un problema
    (ciudad no encontrada o error de red).
    """
    try:
        datos = obtener_coordenadas(ciudad, pais)
    except ConnectionError as error:
        print(f"Error de red: {error}")
        return None

    if datos is None:
        print(f"Ciudad no encontrada: '{ciudad}, {pais}'.")
    return datos


# ---------- Resultado final (Paso 6) ----------

def formatear_distancia(km, unidad):
    """
    Devuelve el texto de la distancia mostrando primero la unidad
    preferida y, entre paréntesis, la otra.
    """
    millas = km_a_millas(km)
    if unidad == "km":
        return f"{km:,.2f} km  ({millas:,.2f} millas)"
    return f"{millas:,.2f} millas  ({km:,.2f} km)"


def mostrar_resultado(origen, destino, unidad):
    """Imprime el resumen final del viaje con distancia y tiempos."""
    km = origen.distancia_a(destino)
    t_avion = formatear_tiempo(calcular_tiempo(km, VELOCIDAD_AVION))
    t_auto = formatear_tiempo(calcular_tiempo(km, VELOCIDAD_AUTO))

    print("\n========== RESUMEN DEL VIAJE ==========")
    print(f"Origen:   {origen.nombre}, {origen.pais}  "
          f"({origen.latitud}, {origen.longitud})")
    print(f"Destino:  {destino.nombre}, {destino.pais}  "
          f"({destino.latitud}, {destino.longitud})")
    if km == 0:
        print("\nNota: el origen y el destino son el mismo lugar.")
    print(f"\nDistancia en línea recta: {formatear_distancia(km, unidad)}")
    print(f"\nTiempo estimado en avión ({VELOCIDAD_AVION} km/h):  {t_avion}")
    print(f"Tiempo estimado en auto  ({VELOCIDAD_AUTO} km/h):   {t_auto}")
    print("\n* La distancia es una aproximación en línea recta, no por carretera.")
    print("=======================================")


def calcular_viaje():
    """Flujo completo de la opción 1. Si algo falla, regresa al menú."""
    ciudad_o = pedir_ciudad("origen")
    pais_o = pedir_pais("origen")
    ciudad_d = pedir_ciudad("destino")
    pais_d = pedir_pais("destino")
    unidad = pedir_unidad()

    mostrar_resumen_entrada(ciudad_o, pais_o, ciudad_d, pais_d, unidad)

    print("Consultando datos...")
    origen = consultar_lugar(ciudad_o, pais_o)
    if origen is None:
        return  # regresa al menú
    destino = consultar_lugar(ciudad_d, pais_d)
    if destino is None:
        return  # regresa al menú

    mostrar_resultado(origen, destino, unidad)


def main():
    """Ciclo principal: repite el menú hasta que el usuario elija salir."""
    print("¡Bienvenido!")
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            try:
                calcular_viaje()
            except Exception as error:
                # Última red de seguridad: el programa nunca se cierra con error
                print(f"Ocurrió un error inesperado: {error}")
        elif opcion == "2":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Elige 1 o 2.")


# Solo se ejecuta al correr main.py directamente
if __name__ == "__main__":
    main()