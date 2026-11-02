
"""
Megan De Leon

main.py - Calculadora de Distancias
"""

## 1. Menú principal
# Pueden agregar mas opciones despues
print("\n=== Mensaje de bienvenida ===")
print("1. Calcular distancia")
print("2. Salir")


## 2. pedir al usuario que eliga una opcion del menu
opcion = input("Elige una opción: ")

## 3. if 1 pedir origen y destino elif salida adios, else no valido.
## 4. dentro del 1 tenemos que pedir ciudad origen y ciudad destino
## 5. luego calcular la distancia... como? coordenadas.  km? millas?
## 6. try except
if opcion == "1":
    # Entrada de datos del usuario
    ciudad_o = input("Ciudad de origen: ")

    # Mostrar resumen
    print("\n--- Resumen ---")
    print(f"Origen:  {ciudad_o}")
    
    # Consulta a la API
    print("Consultando datos...")
   
    # --- BÚSQUEDA DE ORIGEN CON TRY/EXCEPT ---
    
# Resultados
    print("\n--- Coordenadas Obtendas ---")
    # Destino hard coded
    print("Destino: San Marcos, Guatemala - lat 14.9639, lon -91.7944")
    print("Distancia:")


elif opcion == "2":
    print("¡Hasta pronto!")
else:
    print("Opción no válida.")