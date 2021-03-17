class item_seccion:
    def __init__(self, identificador=None,nombre=None,precio=None,cadena=None):
        self.identificador = identificador
        self.precio = precio
        self.cadena= cadena

class seccion:
    def __init__(self,nombre = None,item_seccion = None):
        self.nombre = nombre
        self.item_seccion = item_seccion


class token:
    def __init__(self, token = None,lexema = None, no = None, fila = None, columna = None):
        self.token = token
        self.lexema  = lexema
        self.no = no
        self.fila = fila
        self.columna = columna

class factura:
    def __init__(self,nombre=None,nit=None,direccion=None,porcentaje=None,ordenes=None,tot=None,stt=None,propina=None):
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion 
        self.porcentaje = porcentaje
        self.ordenes = ordenes
        self.tot = tot
        self.stt = stt
        self.propina = propina
class orden:
    def __init__(self, cantidad = None, precio=None,id = None, tt=None, producto = None):
        self.cantidad = cantidad
        self.precio = precio
        self.id = id
        self.tt = tt
        self.producto = producto