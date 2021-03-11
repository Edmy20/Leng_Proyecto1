class item_seccion:
    def __init__(self, identificador=None,nombre=None,precio=None,descripcion=None):
        self.identificador = identificador
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

class seccion:
    def __init__(self,nombre,item_seccion):
        self.nombre = nombre
        self.item_seccion = item_seccion