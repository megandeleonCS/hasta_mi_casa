# Para almacenar la lista
roster = []

# Cargar la lista desde el archivo
try:
    archivoRoster = open('roster.txt', 'r')
    for line in archivoRoster:
        roster.append(line.strip())
    archivoRoster.close()
except FileNotFoundError:
    print('Creando archivo para la lista.')
    archivoRoster = open("roster.txt", "x")
    archivoRoster.close()

while True:
    print(f"\nLista: {roster}")
    print('1. Agregar Nombre\n2. Eliminar Nombre \n3. Salir')
    try:
        eleccion = int(input("Seleccion: "))
    except ValueError:
        break

    if eleccion == 1:
        toAdd = input('Nombre:')
        roster.append(toAdd)
    elif eleccion == 2:
        toRemove = input('Eliminar:')
        try:
            roster.remove(toRemove)
        except:
            print('Error al eliminar')
    else:
        break

# Guarda la lista en el archivo
try:     
    archivoRoster = open('roster.txt', 'w')
    for n in roster:         
        archivoRoster.write(n + '\n')
    archivoRoster.close()
except:
    print('Error al escribir.')