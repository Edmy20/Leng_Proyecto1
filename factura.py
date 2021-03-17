import webbrowser
import datetime

def escribir_factura(bill,restaurante_nombre):
    contenido = ""

    res = "<h2>%s</h2>"
    dat ="<h3>%s</h3>    <p>Datos del Cliente</p>"
    n = "<p>Nombre: %s</p>"
    ni ="<p>Nit: %s</p>"
    di = "<p>Dirección: %s</p>"

    encabezado=   """<table class="default">

                                <tr>
                              
                                  <th>Cantidad</th>
                              
                                  <th>Concepto</th>
                              
                                  <th>Precio</th>

                                  <th>Total</th>
                              
                                </tr>"""
                              
    fila_inicio = "<tr>"
                              
    fila_contenido = "<td>%s</td>"
                              
    fila_final =" </tr>"

    st=  """ <tr>
                                    <th colspan="3">Subtotal:</th>
                              
                                
                                    <td> Q.%s</td>
                                
                                  </tr>"""
    pro1=  """ <tr>
                                    <th colspan="3">Propina: %s</th>"""
                              
                                
    pro2 ="""                                <td> Q.%s</td>
                                
                                  </tr>"""

    ttt=  """ <tr>
                                    <th colspan="3">TOTAL:</th>
                              
                                
                                    <td>%s</td>
                                
                                  </tr>"""



                              
    fin=" </table>"

    today = datetime.date.today()



    contenido = res % (str(restaurante_nombre))
    contenido+="<h3>Factura No.1</h3> "
    contenido+= dat % (str(today))
    contenido+= n % (bill.nombre)
    contenido+= ni % (str(bill.nit))
    contenido+= di % (str(bill.direccion))
    contenido+= encabezado 
    for orden in bill.ordenes:
        contenido+=fila_inicio
        contenido+= fila_contenido %(str(orden.cantidad))
        contenido+= fila_contenido %(str(orden.producto))
        contenido+= fila_contenido %("Q."+str(orden.precio))
        contenido+= fila_contenido %("Q."+str(orden.tt))
        contenido+=fila_final

    contenido+= st % (str(bill.stt))
    contenido+= pro1 % (str(bill.porcentaje)+"%")
    contenido+= pro2 %  (str(bill.propina))
    contenido+= ttt % (str(bill.tot))

    contenido+=fin



    
    return contenido


def crear_html_factura(bill,restaurante_nombre):
  contenido = escribir_factura(bill,restaurante_nombre)
  t = open("Templetes/template_factura.html",'r')
  f = open("Factura.html",'w',encoding="utf-8")
  template = t.read()
  
  cuerpo = template % (contenido)
  f.write(cuerpo)
  t.close()
  f.close()

  webbrowser.open_new_tab('Factura.html')

#--------------------------------------------------------------------------

