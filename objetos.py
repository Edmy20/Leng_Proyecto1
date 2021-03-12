class item_seccion:
    def __init__(self, identificador=None,nombre=None,precio=None,cadena=None):
        self.identificador = identificador
        self.precio = precio
        self.cadena= cadena

class seccion:
    def __init__(self,nombre,item_seccion):
        self.nombre = nombre
        self.item_seccion = item_seccion


class token:
    def __init__(self, token = None,lexema = None, no = None, fila = None, columna = None):
        self.token = token
        self.lexema  = lexema
        self.no = no
        self.fila = fila
        self.columna = columna
