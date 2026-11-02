import json  # Módulo para trabajar con archivos de formato JSON

# --- FUNCIÓN DE LECTURA DE ARCHIVOS ---
def cargar_coordenadas_backup(filepath="coordenadas.json"):
    """
    Abre y lee el archivo JSON local.
    Si el archivo no existe o tiene errores de formato, devuelve un diccionario vacío.
    """
    try:
        # Usamos 'with' para abrir y asegurar que el archivo se cierre automáticamente
        with open(filepath, "r", encoding="utf-8") as archivo:
            return json.load(archivo)  # Convierte el JSON en un diccionario de Python
    except FileNotFoundError:
        print(f"Advertencia: El archivo '{filepath}' no existe.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: El archivo '{filepath}' tiene un formato inválido.")
        return {}

# --- MENÚ DEL PROGRAMA ---
print("\n=== Calculadora de Distancias ===")
print("1. Calcular distancia")
print("2. Salir")

opcion = input("Elige una opción: ")

if opcion == "1":
    # 1. Pedir datos al usuario
    ciudad_o = input("Ciudad de origen: ")
    pais_o = input("País de origen: ")
    ciudad_d = input("Ciudad de destino: ")
    pais_d = input("País de destino: ")
    unidad = input("Unidad (km/millas): ")

    # Normalizar la unidad ingresada por el usuario
    nombre_unidad = "kilómetros" if unidad.lower() == "km" else "millas"

    # 2. Mostrar resumen de la búsqueda
    print("\n--- Resumen ---")
    print(f"Origen:  {ciudad_o}, {pais_o}")
    print(f"Destino: {ciudad_d}, {pais_d}")
    print(f"Unidad:  {nombre_unidad}\n")

    print("Consultando datos...")
    
    # 3. Cargar el diccionario con las coordenadas desde el archivo JSON
    coordenadas_backup = cargar_coordenadas_backup()

    # 4. Buscar el origen y destino combinando Ciudad y País
    clave_origen = f"{ciudad_o}, {pais_o}"
    clave_destino = f"{ciudad_d}, {pais_d}"

    origen = coordenadas_backup.get(clave_origen)
    destino = coordenadas_backup.get(clave_destino)

    # 5. Mostrar resultados
    print("\n--- Resultados ---")
    
    # Verificar y mostrar origen
    if origen:
        print(f"Origen:  {origen['nombre']}, {origen['pais']} → lat {origen['lat']}, lon {origen['lon']}")
    else:
        print(f"No se encontró '{ciudad_o}' en el archivo local.")

    # Verificar y mostrar destino
    if destino:
        print(f"Destino: {destino['nombre']}, {destino['pais']} → lat {destino['lat']}, lon {destino['lon']}")
    else:
        print(f"No se encontró '{ciudad_d}' en el archivo local.")

elif opcion == "2":
    print("¡Hasta pronto!")

else:
    print("Opción no válida.")