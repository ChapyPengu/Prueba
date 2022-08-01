# EVALUACIONES Y ENTREGAS DE ALGORITMOS.

"""
Nombre: Lautaro
# Apellido: Chaparro
# DNI: 49981508

#TEMA UNICO:

# Ejercicio 1:

#   Escribir una función conversora de milimetros a una unidad de longitud. Recibe 
# como parámetro una cantidad de milímetros y como segundo parámetro una cadena que 
# sera la unidad de longitud a convertir. Las unidades de longitud que la función 
# puede recibir son “mm”, ”cm”, “in” y “ft”. 

# Ayuda: el factor de conversión de para el pasaje de mm a in es 1in/25,4mm y en un 
# ft hay 12in.

# Ejercicio 2:

# Escribir una función jubilado(edad, sexo, aportes) que recibe recibe dos parámetros. 
# El primero es la edad de la persona, el segundo es el sexo de la persona y el tercero 
# es un numero que representa los años de aportes de la persona. La función devuelve True 
# si la persona cumple con los requisitos para jubilarse de lo contrario devuelve False.

# Ayuda: Para la ley Argentina una persona adquiere derecho a la jubilación ordinaria 
# si tiene 30 años de aporte, en el caso que la persona sea mujer la edad mínima es de 
# 60 años y en caso de ser hombre la edad mínima es 65 años. La función también coincidiera 
# que si la persona tiene mas de 70 años independientemente de sus aportes o sexo tiene 
# derecho a una jubilación.  

# Ejercicio 3:

# Escribir una función que simule el siguiente experimento: Se tiene una rata en una 
# jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma probabilidad), 
# si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5 minutos vuelve 
# a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula. La rata no aprende, 
# siempre elige entre los 3 caminos con la misma probabilidad, pero quiere su libertad, por lo 
# que recorrerá los caminos hasta salir de la jaula. 

# La función debe devolver el tiempo que tarda la rata en salir de la jaula.

# Ejercicio 4:

# Escribir una funcion count que recibe como parametro un vector junto con un elemento, y devuelve
# la cantidad de apariciones del elemento en el vector.

# Ejercicio 5:

# Escribir una funcion llamada es_potencia que recibe como parametro 2 numeros enteros llamados n y b
y devuelve true si n es potencia de b. por ejemplo es potencia de (8, 2) puesto que dos al cubo es igual a 8.

# Ejercicio 6:

# Escribir un programa que genere un numero aleatorio del 1 al 10 y seguidamente genere un segundo numero aleatorio,
# compruebe si es igual que el primero, y si no lo es genere un nuevo numero hasta que coincida con el primero.
# el programa debe mostrar por pantalla error o acierto segun la comparacion. y una vez que coincidan el programa debe continuar.
"""

from random import *

def convercion_milimetros(milimetros, unidad):
    if unidad == "mm":
        return milimetros
    elif unidad == "cm":
        return milimetros / 100
    elif unidad == "in":
        return milimetros / 2540
    elif unidad == "ft":
        return milimetros / (2540 * 12)

def jubilado(edad, sexo, aportes):
    if sexo == "MUJER" and edad >= 60 and aportes >= 30:
        return True
    elif sexo == "HOMBRE" and edad >= 65 and aportes >= 30:
        return True
    elif edad >= 70:
        return True
    else:
        return False

def es_potencia(n, b):
    while n != b:
        n = n / b
        if n < b:
            return False
    return True

def contador(vector, elemento):
    aux = 0
    for elem in vector:
        if elem == elemento:
            aux += 1
    return aux

def experimento():
    minutos = 0
    encendido = True
    while encendido == True:
        camino_elejido = randrange(1, 4)
        if camino_elejido == 1:
            minutos += 3
        elif camino_elejido == 2:
            minutos += 5
        elif camino_elejido == 3:
            minutos += 7
            encendido = False
    print(f"El raton tardo {minutos} minutos") 

def comparacion_de_numeros():
    encendido = True
    numero1 = randrange(1, 11)
    while encendido == True:
        numero2 = randrange(1, 11)
        if numero1 == numero2:
            print("ACIERTO")
            encendido = False
        elif numero1 != numero2:
            print("ERROR")
def main():
    pass
main()