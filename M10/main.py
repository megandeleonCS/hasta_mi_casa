import sys
import json
# from api import obtener_coordenadas  # Descommentar cuando funcione el API 

# Una funcion solo para fingir ser un API 
def obtener_coordenadas(ciudad, pais):
    return None  # Para simular que hubo una desconeccion del API

# Funcion para leer el JSON data
def cargar_coordenadas_backup(filepath="coordenadas.json"):
    try:
        with open(filepath, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Advertencia: El archivo '{filepath}' no existe.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: El archivo '{filepath}' tiene un formato inválido.")
        return {}

# --- Programa Inicial ---
print("\n=== Calculadora de Distancias ===")
print("1. Calcular distancia")
print("2. Salir")

opcion = input("Elige una opción: ")

if opcion == "1":
    ciudad_o = input("Ciudad de origen: ")
    pais_o = input("País de origen: ")
    ciudad_d = input("Ciudad de destino: ")
    pais_d = input("País de destino: ")
    unidad = input("Unidad (km/millas): ")

    nombre_unidad = "kilómetros" if unidad == "km" else "millas"
    print("\n--- Resumen ---")
    print(f"Origen:  {ciudad_o}, {pais_o}")
    print(f"Destino: {ciudad_d}, {pais_d}")
    print(f"Unidad:  {nombre_unidad}\n")

    print("Consultando datos...")
    
    # Ver data del JSON
    coordenadas_backup = cargar_coordenadas_backup()

    # Query Origen
    origen = obtener_coordenadas(ciudad_o, pais_o)
    if not origen:
        print("API no disponible para origen. Buscando en archivo local...")
        clave = f"{ciudad_o}, {pais_o}"
        origen = coordenadas_backup.get(clave)

    # Query Destinacion
    destino = obtener_coordenadas(ciudad_d, pais_d)
    if not destino:
        print("API no disponible para destino. Buscando en archivo local...")
        clave = f"{ciudad_d}, {pais_d}"
        destino = coordenadas_backup.get(clave)

    # Resultados
    print("\n--- Resultados ---")
    if origen:
        print(f"Origen:  {origen['nombre']}, {origen['pais']} → lat {origen['lat']}, lon {origen['lon']}")
    else:
        print("No se encontró el origen en la API ni en el archivo local.")

    if destino:
        print(f"Destino: {destino['nombre']}, {destino['pais']} → lat {destino['lat']}, lon {destino['lon']}")
    else:
        print("No se encontró el destino en la API ni en el archivo local.")

elif opcion == "2":
    print("¡Hasta pronto!")
else:
    print("Opción no válida.")