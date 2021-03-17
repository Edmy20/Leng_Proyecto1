from archivo import *
from fdamenu import secciones
from fdamenu import tokens
from fdamenu import fda_menu
from fdamenu import nombre_restaurante
from html_menu import *
from html_tokens_menu import crear_html_tokens
from fdafactura import *
from factura import *
from grafo import *

seguir =True

while seguir:
    print("--------------------------Bienvenido: Seleccione una de las siguientes opciones------------------")
    print("1. Cargar Menú")
    print("2. Cargar Orden")
    print("3. Generar Menú")
    print("4. Generar Factura")
    print("5. Generar Arbol")
    print("6. Salir")
    op=input()

    if op=='1':
        print("--------------------------Cargar Menu ------------------------------ ")
        ruta = cargar()
        data_menu = leer(ruta)



    elif op=='2':
        print("-------------------------- Cargar Orden------------------------------")
        ruta = cargar()
        data_ordenes = leer(ruta)
 
    elif op=='3':
        print("-------------------------------Generar Menú----------------------------------------------")
        restaurante = fda_menu(data_menu)

        print("Desea poner un límite en los precios del menú?\n1.SI\n2.NO")
        limite = input()
        if limite == '1':
            print("Por favor ingrese el máximo precio que desea visualizar: ")
            price = float(input())
            crear_html_limite(secciones,restaurante,price)
        elif limite == '2':
            crear_html(secciones,restaurante)
        crear_html_tokens(tokens)


        #for seccion in secciones:
            #print(seccion.nombre," =")
            #for item in seccion.item_seccion:
                #print(item.identificador,";",item.cadena[1],";",item.precio,";",item.cadena[0])
        


    elif op=='4':
        print("--------------------------------------------Generar Factura---------------------------------------")
        fda_factura(data_ordenes)
        buscar_productos(bill,secciones)

        crear_html_factura(bill,restaurante)





    elif op=='5':
        print("----------------------------- Generar Arbol-----------------------------------------")
        letra = "abcdefghijklmñopqstuvwz"
        print(letra[4])

        graficar(secciones,restaurante)


    elif op=='6':
        seguir=False
    else:
        print("ERROR: Por Favor Seleccione una Opción Válida")