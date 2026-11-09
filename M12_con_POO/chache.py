class CacheManager:

    def __init__(self, filepath="M12_con_POO/coordenadas_cache.json"):
        self.filepath = filepath
        self.cache = self._cargar()

    def _cargar(self):
        # loading logic...
        pass

    def obtener(self, clave):
        return self.cache.get(clave)

    def guardar(self, clave, datos):
        self.cache[clave] = datos
        # saving logic...
        pass