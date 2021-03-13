from archivo import *
from menu import secciones
from menu import fda_menu
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
        data = leer(ruta)


    elif op=='2':
        print("-------------------------- Cargar Orden------------------------------")
 
    elif op=='3':
        print("-------------------------------Generar Menú----------------------------------------------")
        tokens = fda_menu(data)
        for seccion in secciones:
            print(seccion.nombre," =")
            for item in seccion.item_seccion:
                print(item.identificador,";",item.cadena[1],";",item.precio,";",item.cadena[0])


    elif op=='4':
        print("--------------------------------------------Generar Factura---------------------------------------")

    elif op=='5':
        print("----------------------------- Generar Arbol-----------------------------------------")


    elif op=='6':
        seguir=False
    else:
        print("ERROR: Por Favor Seleccione una Opción Válida")