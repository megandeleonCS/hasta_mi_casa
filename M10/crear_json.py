import json

# Dictionary structured to match the API output format
coordenadas_backup = {
    "Madrid, España": {"nombre": "Madrid", "pais": "España", "lat": 40.416775, "lon": -3.703790},
    "Barcelona, España": {"nombre": "Barcelona", "pais": "España", "lat": 41.385064, "lon": 2.173403},
    "Buenos Aires, Argentina": {"nombre": "Buenos Aires", "pais": "Argentina", "lat": -34.603722, "lon": -58.381592},
    "Ciudad de México, México": {"nombre": "Ciudad de México", "pais": "México", "lat": 19.432608, "lon": -99.133208}
}

with open("coordenadas.json", "w", encoding="utf-8") as archivo:
    json.dump(coordenadas_backup, archivo, indent=4, ensure_ascii=False)

print("¡Archivo 'coordenadas.json' creado exitosamente!")