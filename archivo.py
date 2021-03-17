from tkinter.filedialog import askopenfilename
from tkinter import Tk
import re
def cargar():
    Tk().withdraw()
    ruta = askopenfilename() 
    return ruta



def leer(ruta):
    archivo = open(ruta,encoding="utf8")
    data = archivo.read()
    archivo.close()

    return data
