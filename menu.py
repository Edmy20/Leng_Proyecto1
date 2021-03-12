from archivo import *
from objetos import *

ruta = cargar()

data = leer(ruta)

tokens = []
def fda_menu(data):
    state = 0
    cache = ""
    cadena = []
    mama = item_seccion()
    precio = 0.0

    pos = 0
    length = len(data)
    columna = 1
    fila = 1
    no =0

    while pos<length:
        char = data[pos]
        char_ASCII = ord(char)
        columna+=1        
    

        if state == 0:
            if char == '?':
                state = 20
            elif char_ASCII == 39:  
               state = 1
            elif char =='[':
                cadena = []
                mama = item_seccion()
                print("-----------------")
                state = 3
            pos+=1
        elif state == 20:
            if cache == 'restaurante':
                print(cache)
                print("Palabra Reservada")
                cache = ""
                state = 0
            else:
                #print(cache)
                cache+=char
            pos+=1
        elif state == 1:
           if char_ASCII == 39:
               state = 2
           else:
                cache+=char
           pos+=1
        elif state == 2:
            #print(cache)
            no+=1
            tk = token("Cadena",cache,no,fila,columna-(len(cache)+2))
            tokens.append(tk)
            cache = ""
            state = 0
            pos+=1
        elif state == 3:
            if char == ']':
                mama.cadena=cadena
               #print(mama.cadena[0])
               # print(mama.cadena[1])
                state = 0
            elif char_ASCII == 39:
                state = 21
            elif char_ASCII >=48 and char_ASCII<=57:
                state = 90
                cache+=char
            pos+=1
        elif state == 4:
            print("{",cache,"}")
            cache = ""
            state = 0
            pos+=1
        elif state == 21:
           if char_ASCII ==39:
               state = 22
           else:
                cache+=char
           pos+=1
        elif state == 22:
            cadena.append(cache)
            cache = ""
            state = 3
            #pos+=1
        elif state == 90:
            if char_ASCII>=48 and char_ASCII<=57 or char_ASCII == 250:
                cache+=char
                pos+=1
            else:
                print(cache)
                cadena.append(cache)
                cache=""
                state = 3

        if char == '\n':
            columna =0
            fila+=1









fda_menu(data)

for tk in tokens:
    print(tk.lexema, tk.fila,tk.columna, tk.no)