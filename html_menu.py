import webbrowser


def escribir_menu(secciones,restaurante_nombre):


    restaurante = """ <divt><center>%s</center></divt> """

    seccion_titulo =   """ <h2>%s</h2>"""
    item_titulo = """ <h3>%s</h23>"""
    item_precio = """         --------------------------------Q.%s</p>"""
    item_descripción =               """<p>%s"""
    contenido = ""
    contenido += restaurante % (restaurante_nombre)
    for seccion in secciones:
        contenido += seccion_titulo % (str(seccion.nombre))
        for item in seccion.item_seccion:
            contenido+= item_titulo % (str(item.cadena[0]))
            contenido+= item_descripción % (item.cadena[1])
            contenido+= item_precio % (str(float(item.precio)))
            

    
    return contenido


def crear_html(secciones,restaurante_nombre):
  contenido = escribir_menu(secciones,restaurante_nombre)
  t = open("Templates/template_menu.html",'r')
  f = open("MENU.html",'w',encoding="utf-8")
  template = t.read()
  
  cuerpo = template % (contenido)
  f.write(cuerpo)
  t.close()
  f.close()

  webbrowser.open_new_tab('MENU.html')

#--------------------------------------------------------------------------

def escribir_menu_limite(secciones,restaurante_nombre,price):


    restaurante = """ <divt><center>%s</center></divt> """

    seccion_titulo =   """ <h2>%s</h2>"""
    item_titulo = """ <h3>%s</h23>"""
    item_precio = """         --------------------------------Q.%s</p>"""
    item_descripción =               """<p>%s"""
    contenido = ""
    contenido += restaurante % (restaurante_nombre)
    for seccion in secciones:
        contenido += seccion_titulo % (str(seccion.nombre))
        for item in seccion.item_seccion:
            if price>=float(item.precio):
                contenido+= item_titulo % (str(item.cadena[0]))
                contenido+= item_descripción % (item.cadena[1])
                contenido+= item_precio % (str(float(item.precio)))
            

    
    return contenido


def crear_html_limite(secciones,restaurante_nombre,price):
  contenido = escribir_menu_limite(secciones,restaurante_nombre,price)
  t = open("template_menu.html",'r')
  f = open("MENU.html",'w',encoding="utf-8")
  template = t.read()
  
  cuerpo = template % (contenido)
  f.write(cuerpo)
  t.close()
  f.close()

  webbrowser.open_new_tab('MENU.html')