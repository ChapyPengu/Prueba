
def join(vector = None, delimitador = None):
    cadena_final = ""
    for cadena in vector:
        cadena_final += cadena + " "
        if delimitador is None:
            pass
        else:
            cadena_final += delimitador + " "
    if cadena_final[-2] == delimitador:
        cadena_final = cadena_final[:-2]
    return cadena_final
def split(cadena = None, delimitador = None):
    res_lista = []
    res_cadena = ""
    if delimitador is None:
        return [cadena]
    cadena = cadena + delimitador
    for x in range(len(cadena)):
        if cadena[x] != delimitador:
            res_cadena += cadena[x]
        elif cadena[x] == delimitador or cadena[x] == cadena[-1]:
            res_lista.append(res_cadena); res_cadena = ""
    return tuple(res_lista)
def pruebas_join():
    print("\033[1;32m" + "PRUEBAS JOIN" + "\033[0;m")
    print("#JOIN CON DELIMITADOR", join(("Curso: 4to Computacion", "Materia: Algoritmos"), "|"))
    print("#JOIN SIN DELIMITADOR", join(("Curso: 4to Computacion", "Materia: Algoritmos")))
    print("#JOIN VECTR MAS LARGO CON DELIMITADOR", join(("Escuela: ET21","Curso: 4to Computacion", "Materia: Algoritmos"), "|"))
    print("#JOIN DELIMITADOR CON ESPACIO", join(("Curso: 4to Computacion", "Materia: Algoritmos"), " | "))
    print("#JOIN SIN VECTOR", join("|"))
    print("#JOIN CON VECTOR DE 2 ESPACIOS", join(("  ")), "|")
    print("#JOIN CON UNA CADENA CON DELIMITADOR", join(("Curso: 4to Computacion Materia: Algoritmos"), "|"))
    print("#JOIN CON UNA CADENA SIN DELIMITADOR", join(("Curso: 4to Computacion Materia: Algoritmos")))
    print("#JOIN CON UN VECTOR QUE CONTIENE EL DELIMITADOR", join(("Curso: 4to Computacion", "| ", "Materia: Algoritmos"), "|"))
    print("#JOIN CON UN VECTOR QUE CONTIENE EN UN UN ELEMENTO EL DELIMITADOR", join(("Curso | 4to | Computacion", "Materia | Algoritmos")))
    print("\033[1;32m" + "PRUEBAS JOIN REALIZADAS CORRECTAMENTE" + "\033[0;m" + "\n")
def pruebas_split():
    print("\033[1;32m" + "PRUEBAS SPLIT" + "\033[0;m")
    print("#SPLIT CON DELIMITADOR", split("Curso: 4to Computacion | Materia: Algoritmos", "|"))
    print("#SPLIT SIN DELIMITADOR", split("Curso: 4to Computacion Materia: Algoritmos"))
    print("#SPLIT UNA CADENA MAS LARGA CON DELIMITADOR", split("Escuela: ET21 Curso: 4to Computacion Materia: Algoritmos", "|"))
    print("#SPLIT DELIMITADOR CON ESPACIO", split("Curso: 4to Computacion Materia: Algoritmos", " | "))
    print("#SPLIT SIN CADENA", split("|"))
    print("#SPLIT CON UNA CADENA VACIA", split(""), "|")
    print("#SPLIT CON UNA CADENA CON DELIMITADOR", split("Curso: ||| 4to Computacion Materia: ||| Algoritmos", "|"))
    print("#SPLIT CON UNA CADENA SIN DELIMITADOR", split("Curso: 4to Computacion Materia: Algoritmos"))
    print("#SPLIT CON UN CADENA QUE CONTIENE UN DELIMITADOR", split("Curso: 4to Computacion |  Materia: Algoritmos"), "|")
    print("#SPLIT CON UN CADENA QUE CONTIENE EN UN UN ELEMENTO EL DELIMITADOR", split("Curso | 4to | Computacion Materia | Algoritmos"))
    print("\033[1;32m" + "PRUEBAS SPLIT REALIZADAS CORRECTAMENTE" + "\033[0;m" + "\n")
def programa_ingresar_y_mostrar_cursos_y_materias():
    lista_de_cursos_y_materia = []
    print("\033[4;31m" + "\033[1;31m "+"####CARACTER DE CORTE: '/'####" + "\033[0;m" + "\n")
    while True:
        curso_ingresado = input("\033[1;32m" + "INGRESE UN CURSO:\n" + "\033[0;m")
        materia_ingresada = input("\033[1;32m" + "INGRESE UNA MATERIA:\n" + "\033[0;m")
        if curso_ingresado == "/" or materia_ingresada == "/":
            break
        lista_de_cursos_y_materia.append(("Curso:" + " " + curso_ingresado, "Materia:" + " " + materia_ingresada))
        ver_o_cargar = int(input("\033[1;35m""1. VER DATOS CARGADOR.\n2. SEGUIR CARGANDO DATOS.\n"+ "\033[0;m"))
        if ver_o_cargar == 1:
                break
    for curso,materia in lista_de_cursos_y_materia:
        print("\033[1;36m" + "#" + curso, "|" ,materia + "\033[0;m")
        print(type(lista_de_cursos_y_materia[0]))
def main():
    pruebas_join()
    pruebas_split()
    programa_ingresar_y_mostrar_cursos_y_materias()
main()