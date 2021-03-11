from archivo import *

ruta = cargar()

data = leer(ruta)

def fda_menu(data):
    state = 0
    cache = ""

    pos = 0
    length = len(data)

    while pos<length:
        char = data[pos]
        
        if state == 0:
            if char =='\'':
               state = 1
            elif char =='[':
                print(char)
                state = 3
            pos+=1

        elif state == 1:
           if char =='\'':
               state = 2
           else:
                cache+=char
           pos+=1
        elif state == 2:
            print(cache)
            cache = ""
            state = 0
            pos+=1
        elif state == 3:
            if char == ']':
                state = 4
            else:
                cache+=char
            pos+=1
        elif state == 4:
            print("{",cache,"}")
            cache = ""
            state = 0
            pos+=1






fda_menu(data)