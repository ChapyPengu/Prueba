# Lista [4, 2, 6, 10, 9, 8, 1, 20, 30, 15, 8, 40, 783, 1, 43, 57, 98, 1, 7, 0, 1, 54, 90].

# Metodo de la burbuja
def burbujeo(vector):
    auxiliar = 0
    for recorrido in range(1 - len(vector)):
        for posicion in range(len(vector) - recorrido):
            if vector[posicion] > vector[posicion + 1]:
                auxiliar = vector[posicion]
                vector[posicion] = vector[posicion + 1]
                vector[posicion + 1] = auxiliar
    return vector

# Metodo recursivo.
def menor_e_indice_en_vector(vector):
    numero_menor = 0
    indice_numero_menor = 0
    for i in range(len(vector) - 1):
        if vector[i] + i == vector[0]:
            numero_menor = vector[i]
        if vector[i] > vector[i + 1]:
            numero_menor = vector[i + 1]
            indice_numero_menor = i + 1
    return numero_menor, indice_numero_menor
def esta_ordernado(vector):
    ordenado = True
    for x in range(len(vector) - 1):
        if vector[x] <= vector[x + 1]:
            continue
        else:
            ordenado = False
            break
    return ordenado
def recursiva(vector):
    estado_vector = esta_ordernado(vector)
    if estado_vector:
        return vector
    menor,indice = menor_e_indice_en_vector(vector)
    vector.pop(indice)
    vector = [menor] + vector
    return recursiva(vector)

# Metodo insercion
def insercion(vector):
    auxiliar = 0
    for x in range(len(vector)):
        for y in range(len(vector)):
            vector[x]
            pass