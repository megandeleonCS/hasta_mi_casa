"""

"""
"""
main.py - Calculadora de Distancias
Versión simplificada sin funciones
"""

import sys
#from api import obtener_coordenadas

# Configuración de codificación para consola Paso 4 y 5 M11
# sys.stdout.reconfigure(encoding="utf-8")


## 1. Menú principal
print("\n=== Calculadora de Distancias ===")
print("1. Calcular distancia")
print("2. Salir")

## 2. pedir al usuario que eliga en un menu
opcion = input("Elige una opción: ")


## 3. if 1 pedir origen y destino elif salida adios, else no valido.

## 4. dentro del 1 tenemos que pedir ciudad origen y ciudad destino
## 5. luego calcular la distancia... como? coordenadas.  km? millas?
## 6. try except
if opcion == "1":
    # Entrada de datos del usuario
    ciudad_o = input("Ciudad de origen: ")
    pais_o = input("País de origen: ")
    ciudad_d = input("Ciudad de destino: ")
    pais_d = input("País de destino: ")
    unidad = input("Unidad (km/millas): ")

    # Mostrar resumen
    nombre_unidad = "kilómetros" if unidad == "km" else "millas"
    print("\n--- Resumen ---")
    print(f"Origen:  {ciudad_o}, {pais_o}")
    print(f"Destino: {ciudad_d}, {pais_d}")
    print(f"Unidad:  {nombre_unidad}")

    # Consulta a la API
    print("Consultando datos...")
    # descomentar el from api import tambien
    #origen = obtener_coordenadas(ciudad_o, pais_o)
    #destino = obtener_coordenadas(ciudad_d, pais_d)
    
    ## Consulta en M11 - build a try/except
    # Consulta a la API
    print("Consultando datos...")
    
    # --- BÚSQUEDA DE ORIGEN CON TRY/EXCEPT ---
    COORDENADAS_CONOCIDAS = {
        "layton": {"lat": 41.0602, "lon": -111.9710},
        "san marcos": {"lat": 14.9639, "lon": -91.7944},
        "madrid": {"lat": 40.4168, "lon": -3.7038}
    }

    COORDENADAS_DEFECTO = {"lat": 0.0, "lon": 0.0}

    try:
        clave_o = ciudad_o.strip().lower()
        if clave_o not in COORDENADAS_CONOCIDAS:
            raise KeyError(f"La ciudad '{ciudad_o}' no existe en la base de datos.")
        
        coords = COORDENADAS_CONOCIDAS[clave_o]
        origen = {
            "nombre": ciudad_o,
            "pais": pais_o,
            "lat": coords["lat"],
            "lon": coords["lon"]
        }
    except KeyError as error:
        print(f"[Aviso] {error} Usando coordenadas por defecto.")
        origen = {
            "nombre": ciudad_o,
            "pais": pais_o,
            "lat": COORDENADAS_DEFECTO["lat"],
            "lon": COORDENADAS_DEFECTO["lon"]
        }

    """
    # Resultados ya con api
    if origen:
        print(f"Origen:  {origen['nombre']}, {origen['pais']} → lat {origen['lat']}, lon {origen['lon']}")
    else:
        print("No se encontró el origen.")

    if destino:
        print(f"Destino: {destino['nombre']}, {destino['pais']} → lat {destino['lat']}, lon {destino['lon']}")
    else:
        print("No se encontró el destino.")
"""
# Resultados
    print("\n--- Coordenadas Obtendas ---")
    print(f"Origen:  {origen['nombre']}, {origen['pais']} → lat {origen['lat']}, lon {origen['lon']}")
    print("Destino: San Marcos, Guatemala - lat 14.9639, lon -91.7944")
    print("Distancia:")


elif opcion == "2":
    print("¡Hasta pronto!")
else:
    print("Opción no válida.")