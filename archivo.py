from tkinter.filedialog import askopenfilename
from tkinter import Tk

def cargar():
    Tk().withdraw()
    ruta = askopenfilename() 
    return ruta



def leer(ruta):
    archivo = open(ruta,'r')
    data = archivo.read()
    archivo.close()

    return data
