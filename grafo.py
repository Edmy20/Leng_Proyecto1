from graphviz import render
from graphviz import Digraph
from graphviz import Graph

def graficar(secciones,restaurante_nombre):

    dot = Digraph()
    dot.node('r',str(restaurante_nombre))

    no = 0
    it = 0

    letra = "abcdefghijklmñopqstuvwzAB"

    for section in secciones:
        no+=1
        dot.node(letra[no],str(section.nombre))
        dot.edge('r',letra[no])
        
        for item in section.item_seccion:
            it+=1
            temp = str(item.cadena[0])+"    Q."+str(item.precio)+"\n"+str(item.cadena[1])
            dot.node(str(it),temp)
            dot.edge(letra[no],str(it))




    dot.render('grafo')

