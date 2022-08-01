# Python
# Portafolio (Parte 2)

# Paso 0: Crear un contexto
from datetime import datetime
from django.template import Template, Context, loader

datos_contexto = {"fecha_actual" : datetime.now(), "username" : "ChapyPenegu"}

# Paso 0: Crear el contexto
datos = {"notas" : [7, 4, 10, 3, 8, 5]}

# Paso 1: Cargar contenido HTML
archivo = open(r"C:\Users\chapa\OneDrive\Escritorio\Lautaro Chaparro ._.(CHAP)._\Coder_python\index.html")
contenido = archivo.read()
archivo.close()

# Paso 2: Crear contexto
contexto = Context(datos)

# Nueva vista
def alumnos(request):
    pass