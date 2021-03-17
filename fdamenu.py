from archivo import *
from objetos import *
import webbrowser

def ingresar_data():
    ruta = cargar()
    data = leer(ruta)

    return data
tokens = []
nombre_restaurante  = ""
secciones = []
sec = seccion()
def fda_menu(data):

#----------------------------Variables del Adf--------------------------------------
    state = 0
    cache = ""
    pos = 0
    length = len(data)

#--------------------------------Posicion de tokens--------------------------------
    columna = 0
    fila = 1
    no_token = 0
    no_error = 0


#---------------------------Variables Para Objetos------------------------------
    asig = False
    asig_r = False
    section = False
    opciones_menu = False
    temp= 0
    nombre = ""
    cadena = []
    item = item_seccion()
    precio = 0.0
    identificador = ""
    items = []



    while pos<length:
        char = data[pos]
        char_ASCII = ord(char)
        columna+=1
        tk = token()
        if state == 0:
            if char_ASCII == 114:
                cache+=char
                pos+=1
                state = 1
            elif char_ASCII == 58:
                #print("Token_dosPuntos = ",char)
                no_token+=1
                tk = token("Dos Puntos",char,no_token,fila,columna)
                tokens.append(tk)
                pos+=1
            elif char_ASCII == 59:
                #print("Token_PuntoyComa = ",char)
                no_token+=1
                tk = token("Punto y Coma",char,no_token,fila,columna)
                tokens.append(tk)
                pos+=1
            elif char_ASCII == 61:
                #print("Token_Asignación = ",char)
                no_token+=1
                tk = token("Asignación",char,no_token,fila,columna)
                tokens.append(tk)
                pos+=1
            elif char_ASCII == 91:
               # print("Token_abrirCorchete = ",char)           
                no_token+=1
                tk = token("Abrir Corchete",char,no_token,fila,columna)
                tokens.append(tk)
                pos+=1
            elif char_ASCII == 93:
                #print("Token_cerrarCorchete = ",char)
                no_token+=1
                tk = token("Cerrar Corchete",char,no_token,fila,columna)
                tokens.append(tk)
                pos+=1
            elif char_ASCII == 114:
                state = 1
                pos+=1
            elif char_ASCII == 39:
                state = 12
                pos+=1
            elif char_ASCII >= 48 and char_ASCII<= 57:
                state = 15
            elif char_ASCII >=97 and char_ASCII<=122:
                state = 14
            elif char_ASCII == 32:
                pos+=1
            elif char == '\n':
                fila+=1
                columna = 0
                pos+=1
            else:
                #print("ERROR: Carácter ",char," no reconocido")
                pos+=1
        elif state == 12:
            if char_ASCII == 39:
                state = 13
            else:
                cache+=char
                pos+=1
        elif state == 13:
            #print("Token_Cadena: ", cache)
            no_token+=1
            tk = token("Cadena",cache,no_token,fila,columna)
            tokens.append(tk)
            cache=""
            state = 0
            pos+=1
        elif state == 14:
            if char_ASCII >= 97 and char_ASCII<= 122 or char_ASCII == 95:
                cache+=char
                pos+=1
            elif char_ASCII >=48 and char_ASCII<=57:
                cache+=char
                pos+=1
            else:
                #print("Identificador: ",cache)
                no_token+=1
                tk = token("Identificador",cache,no_token,fila,columna)
                tokens.append(tk)
                cache=""
                state=0
        elif state== 15:
            if char_ASCII >= 48 and char_ASCII <= 57:
                cache+=char
                pos+=1
            elif char_ASCII == 46:
                cache+=char
                pos+=1
            else:
                #print("Token_numero: ",cache)
                no_token+=1
                tk = token("numero",cache,no_token,fila,columna)
                tokens.append(tk)
                cache=""
                state=0

        elif state == 1:
            if char_ASCII == 101:
                cache+=char
                state = 2
                pos+=1
            else:
                print("Error: ", cache, "no es una palabra reservada")
                state  = 0
            
        elif state == 2:
            if char_ASCII == 115:
                cache+=char
                state = 3
                pos+=1
            else:
                print("Error: ", cache, "no es una palabra reservada")
                state  = 0
        elif state == 3:
            if char_ASCII == 116:
                cache+=char
                state = 4
                pos+=1
            else:
                print("Error: ", cache, "no es una palabra reservada")
                state  = 0
        elif state == 4:
            if char_ASCII == 97:
                cache+=char
                state = 5
                pos+=1
            else:
                print("Error: ", cache, "no es una palabra reservada")
                state  = 0
        elif state == 5:
            if char_ASCII == 117:
                cache+=char
                state = 6
                pos+=1
            else:
                print("Error: ", cache, "no es una palabra reservada")
                state  = 0
        elif state == 6:
            if char_ASCII == 114:
                cache+=char
                state = 7
                pos+=1
            else:
                print("Error: ", cache, "no es una palabra reservada")
                state  = 0
        elif state == 7:
            if char_ASCII == 97:
                cache+=char
                state = 8
                pos+=1
            else:
                print("Error: ", cache, "no es una palabra reservada")
                state  = 0
        elif state == 8:
            if char_ASCII == 110:
                cache+=char
                state = 9
                pos+=1
            else:
                print("Error: ", cache, "no es una palabra reservada")
                state  = 0
        elif state == 9:
            if char_ASCII == 116:
                cache+=char
                state = 10
                pos+=1
            else:
                print("Error: ", cache, "no es una palabra reservada")
                state  = 0
        elif state == 10:
            if char_ASCII == 101:
                cache+=char
                state = 11
                pos+=1
            else:
                print("Error: ", cache, "no es una palabra reservada")
                state  = 0
        elif state == 11:
            #print("Palabra_Reservada =  ",cache)
            no_token+=1
            tk = token("Palabra Reservada",cache,no_token,fila,columna)
            tokens.append(tk)
            cache = ""
            state = 0
        
        

        if tk.token == "Palabra Reservada":
            asig_r = True
        elif asig_r == True and tk.token == "Asignación":
            asig = True
            asig_r = False
        elif asig == True and tk.token == "Cadena":
            global nombre_restaurante 
            nombre_restaurante = tk.lexema
            asig = False
        elif tk.token == "Dos Puntos":
            global sec 
            sec = seccion()
            sec.nombre = temp
            items = []
            secciones.append(sec)
            section = True
        elif tk.token == "Abrir Corchete":
            cadena = []
            item = item_seccion()
            opciones_menu = True
        elif tk.token == "Cadena" and opciones_menu == True:
            cadena.append(tk.lexema)
        elif tk.token == "Identificador" and opciones_menu == True:
            item.identificador = tk.lexema
        elif tk.token == "numero" and opciones_menu == True:
            item.precio = tk.lexema
        elif tk.token == "Cerrar Corchete" and opciones_menu == True:
            item.cadena = cadena
            items.append(item)
            sec.item_seccion = items
            opciones_menu = False
            section = False       
        elif tk.token == "Cadena" and section == False:
            temp = tk.lexema
        
    return nombre_restaurante

            
                    
        

            
        

#d = ingresar_data()
            
#f = fda_menu(d)

#for tk in tokens:
    #print(tk.token," / ",tk.lexema," /",tk.no," f: ",tk.fila,"c:",tk.columna)

##print(f)

#for secs in secciones:
    #print(secs.nombre)
    #for item in secs.item_seccion:
        #t= item.precio+" ;"+item.identificador+"; "
        #print(t,end = " ")
        #for c in item.cadena:
            #print(c)
