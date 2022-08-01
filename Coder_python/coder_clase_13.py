
# Programacion orientada a objetos

# Objetos, Estos se creean atravez de una clase.
# Cada vez que se creea un objeto, Cada uno es distinto entre si.
# Es importante para moduloralizar un problema. Ejemplo algoritmo para recomendar una serie.
# Dentro de paython, todo es un objeto.
# 
# Clases: 
# Lo primero es crear una clase
# Definir clase.
class perro:
    pass

    # Atributos de clase
    especie = "Mamifero"

    # Constructor, self es una variable que hace referencia al objeto a crear.
    def __init__(self, edad, nombre, raza):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

# Instanciar clase.
perrito1 = perro(3, "Mofletes", "Canichi")
perrito2 = perro(19, "Joan", "Labrador")


print(type(perrito1),id(perrito1))
print(type(perrito2),id(perrito2))

print(perrito1.especie)

# Mi Primera clase.

import pstats


class persona:
    
    accion = "Cliente"
    especie = "Reptiliano"
    nacionalidad = "Argentina"
    idioma = "Espaniol"

    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def hablar(self, mensaje):
        print(f"Mensaje de {self.nombre}: {mensaje}")

agustin = persona("agustin", "jerez", 74, "machoo")
print(agustin.hablar(""))

class Animal:
    def __init__(self, especie : str, alimentacion : str, tiene_pelo : bool, patas : int):
        self.especie = especie
        self.alimentacion = alimentacion
        self.tiene_pelo = tiene_pelo
        self.patas = patas
    def comunicarse(self):
        pass
    def reproducirce(self):
        pass
    def comer(self):
        pass
    def moverce(self):
        pass
    def __str__(self) -> str:
        return f"Soy un animal {self.especie}. Me alimento de {self.alimentacion} y tengo {self.patas}"

class perro(Animal):
    pass


from curses import raw
import sys

def validar_numero(numero):
    if 0 <= numero <= 10:
        return True
    else:
        return False

if len(sys.argv) == 3:
    numero1 = int(sys.argv[1])
    numero2 = int(sys.argv[2])

    if validar_numero(numero1) and validar_numero(numero2):
        if numero1 >= 7 and numero2 >= 7:
            print("PROMOCIONADO")
        elif numero1 >= 4 and numero2 >= 4:
            print("APROBADO")
        elif numero1 < 4 or numero2 < 4:
            if numero1 < 3:
                print("DESAPROBADO, DEBE RENDIR EL PRIMER PARCIAL")
            else:
                print("DESAPROBADO, DEBE RECUPERAR EL SEGUNDO PARCIAL")
        elif numero1 < 4 and numero2 < 4:
            print("DESAPROBO AMBOS PARCIALES, DEBE RECURSAR")
else:
    print("USO DEL SCRIPT: DESAFIO.PY <VALOR1> <VALOR2>")

