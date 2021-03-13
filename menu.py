from archivo import *
from objetos import *
import webbrowser
ruta = cargar()
data = leer(ruta)

secciones = []
errores = []
def fda_menu(data):
#----------------------------Variables del Adf--------------------------------------
    state = 0
    cache = ""
    pos = 0
    length = len(data)

#--------------------------------Posicion de tokens---------------------------
    columna = 1
    fila = 1
    no =0
    no_error = 0
#---------------------------Variables Para Objetos------------------------------
    nombre = ""
    cadena = []
    item = item_seccion()
    precio = 0.0
    identificador = ""
    tokens = []
    items = []
    sec = seccion()

    while pos<length:
        char = data[pos]
        char_ASCII = ord(char)
        columna+=1     

#--------------------------------------' Estado Inicial '-----------------------------
        if state == 0:
            if char == '?':
                cache+=char
                state = 1
#------------------------------------- ' '--------------------------------------
            elif char_ASCII == 39 and fila!=1:
                sec = seccion()#Inicia una sección
                items = []
                secciones.append(sec)
                state = 11
#-----------------------------------' [ '--------------------------------------------
            elif char =='[':
                cadena = []#Se abre una nueva lista de cadenas
                state = 3
#----------------------------------- : ------------------------------------------
            elif char_ASCII == 58:
                 no+=1
                 tk = token("Dos puntos",char,no,fila,columna)
                 tokens.append(tk)
                 state = 0

            pos+=1
#-----------------------------------Restaurante---------------------------------------
        elif state == 1:
            cache = data[pos:pos+10]
            print(cache)
            state = 0

            pos+=10
#---------------------------------' ' -----------------------------------------------------
        elif state == 11:
           if char_ASCII == 39:
               state = 2
           else:
                cache+=char
           pos+=1
#---------------------------- cerrar '-------------------------------------------
        elif state == 2:
#---------------------Agregar item a de seccion------------------------------
            nombre = cache
            sec.nombre = nombre
#------------------------Registrar Token------------------------------
            no+=1
            tk = token("Cadena",cache,no,fila,columna-(len(cache)+2))
            tokens.append(tk)

            cache = ""
            state = 0
#---------------------------  [------------------------------------
        elif state == 3:
            if char == ']':
                #Creación de un nuevo Item
                item=item_seccion(identificador=identificador,cadena=cadena,precio=precio)
                items.append(item)
                sec.item_seccion = items
                state = 0
            #--------Precio
            elif char_ASCII >=97 and char_ASCII<=122:
                cache+=char
                state = 45
            #----------Cadena
            elif char_ASCII == 39:
                state = 21
            #--------Identificador
            elif char_ASCII >=48 and char_ASCII<=57:
                state = 90
                cache+=char
            elif char == ';':
                no+=1
                tk = token("Punto y Coma",char,no,fila,columna)
                tokens.append(tk)              
            pos+=1
        elif state == 4:
            #print("{",cache,"}")
            cache = ""
            state = 0
            pos+=1
        #----------cadena
        elif state == 21:
           if char_ASCII ==39:
               state = 22
           else:
                cache+=char
           pos+=1
        #-----------cerrar cadena
        elif state == 22:
            cadena.append(cache)
            cache = ""
            state = 3
        #-------precio

        elif state == 90:
            if char_ASCII>=48 and char_ASCII<=57 or char == '.':
                cache+=char
                pos+=1
            else:
                precio = cache
                cache=""
                state = 3
        #-----identificador
        elif state == 45:
            if char_ASCII >=97 and char_ASCII<=122:
                cache+=char
                pos+=1
            elif char_ASCII>=48 and char_ASCII<=57 or char == '_':
                cache+=char
                pos+=1
            #elif char_ASCII == 255 or char == ';':
                #identificador = cache
                #cache = ""
                #state=3
            else:
                #cache+=char
                #state = 89
                #pos+=1
                identificador = cache
                cache = ""
                state=3
            
        elif state == 89:
            if char == ';':
                tk_error = token("Identificador no Válido",cache,no_error,fila,columna)
                errores.append(tk_error)
                state == 3
            else:
                cache+=char
                pos+=1



        if char == '\n':
            columna =0
            fila+=1

    return tokens


tokens = fda_menu(data)

for tk in tokens:
   print(tk.lexema, tk.fila,tk.columna, tk.no)

for seccion in secciones:
    print(seccion.nombre," =")
    for item in seccion.item_seccion:
        print(item.identificador,";",item.cadena[1],";",item.precio,";",item.cadena[0])

for tk_error in errores:
    print("%")


def escribir_menu(secciones):
    titulo =   """  <div class="title">
                        <h3><span>%s</span></h3>
                    </div> """
    item_titulo = """
                            <ul>
                                <li class="wow fadeInUp" data-wow-duration="300ms" data-wow-delay="300ms">
                                    <div class="item">
                                        <div class="item-title">
                                            <h2>%s</h2>"""
    item_precio = """                                           
                                            <div class="border-bottom"></div>
                                            <span>%s</span>
                                        </div>
                                        """
    item_descripción =               """<p>%s</p>
                                    </div>
                                </li>
                            </ul>"""
    contenido = ""
    for seccion in secciones:
        contenido += titulo % (seccion.nombre)
        for item in seccion.item_seccion:
            contenido+= item_titulo % (item.cadena[0])
            contenido+= item_precio % (str(float(item.precio)))
            contenido+= item_descripción % (item.cadena[1])

    
    return contenido


def crear_html(secciones):
  contenido = escribir_menu(secciones)
  t = open("menu.html",'r')
  f = open("PRACTICA UNICA.html",'w')
  template = t.read()
  
  cuerpo = template % (contenido)
  f.write(cuerpo)
  t.close()
  f.close()

  webbrowser.open_new_tab('PRACTICA UNICA.html')

##crear_html(secciones)