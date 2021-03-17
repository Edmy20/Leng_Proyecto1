import webbrowser


def escribir_tabla_tokens(tokens):

    encabezados = """<table class="default">

                            <tr>

                                <th scope="row">No.</th>

                                <th>Lexema</th>

                                <th>Fila</th>

                                <th>Columna</th>

                                <th>Token</th>

                            </tr>"""
        
    no_tk = """              <tr>

                                <th>%s</th>"""
        
    tk_fila =             """ <td>%s</td>"""


    fin_fila=                   """ </tr>"""


    fin      =            """ </table>"""


    contenido = encabezados

    for tk in tokens:
        contenido+= no_tk % (str(tk.no))
        contenido+= tk_fila % (str(tk.lexema))
        contenido+= tk_fila % (str(tk.fila))
        contenido+= tk_fila % (str(tk.columna))
        contenido+= tk_fila % (str(tk.token))
        contenido+= fin_fila
    

    contenido += fin



    
    return contenido


def crear_html_tokens(tokens):
  contenido = escribir_tabla_tokens(tokens)
  t = open("Templetes/template_tokens.html",'r')
  f = open("Tabla Tokens.html",'w',encoding="utf-8")
  template = t.read()
  
  cuerpo = template % (contenido)
  f.write(cuerpo)
  t.close()
  f.close()

  webbrowser.open_new_tab('Tabla Tokens.html')
