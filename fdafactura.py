from archivo import *
from objetos import *



def ingresar_data():
    ruta = cargar()
    data = leer(ruta)

    return data

tokens_factura = []
bill = factura()
def fda_factura(data):
    #data = ingresar_data()
#----------------------------Variables del Adf--------------------------------------
    state = 0
    cache = ""
    pos = 0
    length = len(data)
    columna = 1
    fila = 1
    no_token = 0

    orders = []
    op  = 0
    porcen = 0
    order = orden()
    su = 0





    while pos<length:
        char = data[pos]
        char_ASCII = ord(char)
        tk = token()


        if state == 0:
            if char_ASCII == 39:
                state = 1
                pos+=1
                columna+=1
            elif char_ASCII >= 97 and char_ASCII <= 122:
                state = 3
            elif char_ASCII >=48 and char_ASCII <= 57:
                state = 4
            elif char_ASCII == 44:
                #print("Token_coma: ",char)
                no_token+=1
                tk = token("Coma",char,no_token,fila,columna)
                tokens_factura.append(tk)
                pos+=1
                columna+=1
            elif char_ASCII == 32:
                pos+=1
                columna+=1

            elif char == '\n':
                fila+=1
                columna =1
                pos+=1
            else:
                #print("Error: Caracter ",char," no pertenece al lenguaje")
                pos+=1
                columna+=1

        elif state == 1:
            if char_ASCII == 39:
                state = 2
            else:
                cache+=char
                pos+=1
                columna+=1
        elif state == 2:
            #print("Token_Cadena: ", cache)
            no_token += 1
            op+=1
            tk = token("Cadena",cache,no_token,fila,columna-len(cache))
            tokens_factura.append(tk)
            cache=""
            state = 0
            pos+=1
            columna+=1


        elif state == 3:
            if char_ASCII >= 97 and char_ASCII <= 122 or char_ASCII == 95:
                cache+=char
                pos+=1
                columna+=1
            elif char_ASCII >=48 and char_ASCII <= 57:
                cache+=char
                pos+=1
                columna+=1
            else:
                #print("Token_Identificador = ",cache)
                no_token += 1
                tk = token("Identificador",cache,no_token,fila,columna-(len(cache)))
                tokens_factura.append(tk)
                cache = ""
                state = 0

        elif state == 4:
            if char_ASCII >=48 and char_ASCII <= 57:
                cache+=char
                pos+=1
                columna+=1
            elif char_ASCII == 37:
                state = 6
                cache+=char
            elif char_ASCII == 46:
                state = 5
                cache+=char
                pos+=1
                columna+=1
            else:
                #print("Token_numero = ",cache)
                no_token += 1
                no_token += 1
                tk = token("Numero",cache,no_token,fila,columna-(len(cache)))
                tokens_factura.append(tk)
                cache=""
                state = 0
        elif state == 5:
            if char_ASCII >=48 and char_ASCII <= 57:
                cache+=char
                pos+=1
                columna+=1
            elif char_ASCII == 37:
                state = 6
                porcen = cache
                cache+=char
            else:
                print("ERROR: ",cache," no es una cantidad valida")
                state = 0
                cache =""

        elif state == 6:
            #print("Token_porcentaje = ", cache)
            no_token += 1
            tk = token("Porcentaje",cache,no_token,fila,columna-(len(cache)))
            tokens_factura.append(tk)
            cache=""
            state=0
            pos+=1
            columna+=1
        

        if tk.token == "Cadena" and op == 1:
            bill.nombre=tk.lexema
        elif tk.token == "Cadena" and op ==2:
            bill.nit = tk.lexema
        elif tk.token == "Cadena" and op ==3:
            bill.direccion = tk.lexema
            op=0 
        elif tk.token == "Porcentaje":
            bill.porcentaje = porcen
        elif tk.token == "Numero":
            order = orden()
            order.cantidad=tk.lexema
            orders.append(order)
        elif tk.token == "Identificador":
            order.id = tk.lexema
            bill.ordenes = orders

            

def buscar_productos(bill,secciones):
    for orden in bill.ordenes:
        for section in secciones:
           for item in section.item_seccion:
               if orden.id == item.identificador:
                   orden.precio = float(item.precio)
                   orden.producto = item.cadena[0]
                   
    
    total = 0.0
    for orden in bill.ordenes:
        orden.tt = float(orden.cantidad)*orden.precio
        total += orden.tt
        print(orden.tt)

    
    subtotal  = 0.0
 
    bill.stt = total

    pro = total*(float(bill.porcentaje)/100)

    total = total+subtotal

    bill.tot = total   

    bill.propina = pro


        


#fda_factura()
#for tk in tokens_factura:
    #print(tk.lexema)

#print(bill.porcentaje)
#print(bill.nit)
#print(bill.nombre)
#print(bill.direccion)

#for on in bill.ordenes:
    #print(on.id," |",on.cantidad)

