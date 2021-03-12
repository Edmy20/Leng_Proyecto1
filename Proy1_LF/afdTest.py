tokens  = []

#line = 'La musica de Minecraft combina con cualquier situacion'

line = "124g1"


def tda(line):
    #line = str(line)
    state = 0
    cache = ''

    posX = 0
    #posY = 0
    length = len(str(line))

    while posX < length:
        char = line[posX]
        charASCII = ord(char)
        #--------------------SWITCH------------------------
        if state == 0:
            if charASCII >= 48 and charASCII <= 57:
                cache += chr(charASCII)
                state = 1
            else:
                print("Hubo un error: ",cache, " no esta identificado como token") 
        elif state == 1:
            if charASCII >= 48 and charASCII <= 57:
                cache += chr(charASCII)
            else:
                cache += chr(charASCII)
                print("Hubo un error: ",cache, " no esta identificado como token\n")
                cache = "error lexico"
                break
        posX += 1

    print(cache)
tda(line)
