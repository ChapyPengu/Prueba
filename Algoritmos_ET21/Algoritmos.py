from random import *
import this
from time import *
from math import *

def producto(a, b):
    return a * b
def programa_producto():
    a = float(input("Ingrese un valor a multiplcar"))
    b = float(input("Ingrese el siguente valor a multiplicar"))
    resultado = producto(a, b)
    print(("El resultado es: ", resultado))
def perimetro_rectangulo(base, altura):
    return (base * 2)+ (altura * 2)
def area_rectangulo(base, altura):
    return base * altura
def area_rectangulo_cordenadas(x1, x2, y1, y2):
    return (((x1 - x2) ** 2) ** (1/2)) * (((y1 - y2) ** 2) ** (1/2))
def perimetro_circulo(radio):
    return (radio * 2 * 3.14)
def area_ciruclo(radio):
    return (radio ** 2) * 3.14
def volumen_esfera(radio):
    return (4/3) * 3.14 * (radio ** 3)
def hipotenusa_rectangulo(cateto_opuesto, cateto_adyacente):
    return ((cateto_adyacente ** 2) + (cateto_opuesto ** 2)) ** (1 / 2)
def verificacion():
    for i in range(5):
        print(i * i)
    for i in range(2, 6):
        print(i, 2 ** i)
def factorial(n):
    resultado = 1
    for x in range(1, n + 1):
        resultado *= x
    return resultado
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def divicion(a, b):
    if a == 0 or b == 0:
        return 0
    return a / b
def imprimir_por_cantidad(imprimir, cantidad):
    for cantidad_imprimida in range(0, cantidad):
        print(imprimir, end="")
def monto(cantidad_de_pesos, tasa_de_interes, años):
    return cantidad_de_pesos * (1 + (tasa_de_interes / 100)) * años
def programa_monto():
    cantidad_de_pesos = int(input("Ingrese la cantidad de pesos: \n"))
    tasa_de_interes = int(input("Ingrese la tasa de interes: \n"))
    años = int(input("Ingrese los años"))
    monto_final = monto(cantidad_de_pesos, tasa_de_interes, años)
    print(monto_final)
def fahrenheit_a_celcius(grados_celcius):
    return (9/5) * grados_celcius + 32
def programa_fahrenheit_a_celcius():
    for grados in range(0, 120, 10):
        print(fahrenheit_a_celcius(grados))
def par_impar(n):
    if n % 2 == 0:
        return 1
    elif n % 2 != 0:
        return 0
def cantidad_de_digitos(numero):
    numero = ((numero ** 2) ** (1 / 2))
    numeros = {0 : 1, 1 : 9, 2 : 99, 3 : 999, 4 : 9999, 5 : 99999, 6 : 999999, 7 : 9999999, 8 : 99999999, 9 : 999999999, 10 : 9999999999, 11 : 99999999999, 12 : 999999999999}
    for clave in numeros:
        if numero >= numeros[clave] and numero <= numeros[clave + 1]:
            print("El numero posee", clave + 1, "digitos")
def cantidad_de_digitos_2(numero):
    numero = str(numero)
    return len(numero)
def devolver_multiplo_de_10(numero):
    if numero % 10 != 0:
        numero = numero - 1
        devolver_multiplo_de_10(numero)
    else:
        return numero
def numeros_pares(inicio, fin):
    for rango in range(inicio, fin + 1):
        if rango % 2 == 0:
            print(rango)
def numeros_triangulares(numero):
    indice = 0
    acumulador = 0
    for _ in range(0, numero):
        resultado = indice + 1 + acumulador
        indice += 1
        acumulador = resultado
        print(indice, resultado)
def programa_factorial():
    cantidad_de_factorial = int(input("Ingrese la cantidad de factorailes a realizar:\n"))
    for numero in range(1, cantidad_de_factorial + 1):
        resultado = factorial(numero)
        print(resultado)
def programa_imprimir_fichas_de_domino():
    fichas = int(input("Ingrese la cantidad de fichas:\n"))
    inicio = -1
    for ficha in range(0, fichas + 1):
        inicio += 1
        for valor_ficha in range(inicio, fichas + 1):
            print(ficha, valor_ficha)
def convertir_segundos_a_tiempo(segundos_ingresados):
    return (segundos_ingresados // 3600), (segundos_ingresados % 3600) // 60, (segundos_ingresados % 3600) % 60
def convertir_tiempo_a_segundos(horas_ingresadas, minutos_ingresados, segundos_ingresados):
    return (horas_ingresadas * 3600) + (minutos_ingresados * 60) + segundos_ingresados
def programa_suma_de_tiempo():
    acumulador_minutos = 0
    acumulador_horas = 0
    inicio_horas = int(input("Ingrese horas:\n"))
    fin_horas = int(input("Ingrese horas:\n"))
    inicio_minutos = int(input("Ingrese minutos:\n"))
    fin_minutos = int(input("Ingrese minutos:\n"))
    inicio_segundos = int(input("Ingrese segundos:\n"))
    fin_segundos = int(input("Ingrese segundos:\n"))
    tiempo_final = [inicio_horas + fin_horas, inicio_minutos + fin_minutos, inicio_segundos + fin_segundos]
    while tiempo_final[2]>= 60:
        tiempo_final[2] -= 60
        acumulador_minutos += 1
    tiempo_final[1] = tiempo_final[1] + acumulador_minutos
    while tiempo_final[1] >= 60:
        tiempo_final[1] -= 60
        acumulador_horas += 1
    tiempo_final[0] = tiempo_final[0] + acumulador_horas
    print(tiempo_final[0], tiempo_final[1], tiempo_final[2])
def devolver_el_mayor_producto(n1, n2, m1, m2):
    if n1 * n2 == m1 * m2:
        return "Son iguales"
    elif n1 * n2 > m1 * m2:
        return n1 * n2
    return m1 * m2
def norma(x, y, z):
    return ((x*x) + (y*y) + (z*z)) ** (1/2)
def diferencia(x, y, z, x1, y1, z1):
    diff_x = x - x1
    diff_y = y - y1
    diff_z = z - z1
    return diff_x, diff_y, diff_z
def productoVectorial(x1, y1, z1, x2, y2, z2):
    x_Vectoiarl = y1*z2 - z1*y2
    y_Vectorial = z1*x2 - x1*z2
    z_Vectorial = x1*y2 - y1*x2
    return x_Vectoiarl, y_Vectorial, z_Vectorial
def areaTrinaguloVectorial(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    ab = diferencia(x2, y2, z2, x1, y1, z1)
    ac = diferencia(x3, y3, z3, x1, y1, z1)
    producto = productoVectorial(ab[0], ab[1], ab[2], ac[0], ac[1], ac[2])
    modulo = norma(producto[0], producto[1], producto[2])
    modulo = modulo / 2
    return modulo
def area_cuadrilatero(x1, y1, x2, y2, x3, y3, x4, y4):
    print("xd")
def es_par(num):
    return num % 2 == 0
def es_impar(num):
    return num % 3 == 0
def valor_absoluto(num):
    return (num ** 2) ** (1 / 2)
def imprimir_matriz_identidad(dimencion):
    matriz_identidad = []
    lista = []
    acumulador = 0
    for _ in range(0, dimencion):
        matriz_identidad.append(1)
        for _ in range(0, dimencion):
            matriz_identidad.append(0)
    for _ in range(0, dimencion):
        lista.append([])
    for j in range(0, dimencion):
        for x in range(0, dimencion):
            acumulador += j
            for y in range(0, dimencion - 2):
                lista[x].append(matriz_identidad[y + acumulador])
    print(lista)
def polinomio_de_segundo_grado(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "No tiene solucion"
    if ((b ** 2) - 4 * a * c) < 0:
        return "No tiene solucion"
    x1 = (-b + ((b ** 2) - 4 * a * c)) / (2 * a)
    x2 = (-b - ((b ** 2) - 4 * a * c)) / (2 * a)
    return x1, x2
def area_cuadrilatero():
    print("Ejercicio 3.4, e")
def polinomios():
    print("ejercicio4.4, a, b, c, e")
def es_biciesto(año):
    return (año % 4 == 0 and año % 100 == 0 and año % 400 == 0 ) or (año % 4 == 0 and not año % 100 == 0)
def programa_fecha_correcta():
    dia = int(input("INGRESE UN DIA.\n"))
    mes = int(input("INGRESE UN MES.\n"))
    año = int(input("INGRESE UN AÑO.\n"))
    meses_31 = [1, 3, 5, 7, 8, 10, 12]
    meses_30 = [4, 6, 9, 11]
    if dia > 0 and dia <= 31 and mes > 0 and mes <= 12:
        if mes in meses_31:
            print("La fecha existe😈\n", dia,"-",mes,"-",año)
        elif mes == 2 and dia <= 29 and es_biciesto(año):
                print("La fecha existe😈\n", dia,"-",mes,"-",año, "Es bisiesto")
        elif mes == 2 and dia < 29:
            print("La fecha existe😈\n", dia,"-",mes,"-",año) 
        elif dia < 31 and (mes in meses_30):
            print("La fecha existe😈\n", dia,"-",mes,"-",año)
        else:
            print("La fecha no existe 😅")
    else:
        print("La fecha no existe 😅")
def validar_fecha(dia, mes, año):
    MESES_DE_31 = [1, 3, 5, 7, 8, 10, 12]
    MESES_DE_30 = [4, 6, 9, 11]
    if dia > 0 and dia <= 31 and mes > 0 and mes <= 12:
        if mes in MESES_DE_31:
            return True
        elif mes == 2 and dia <= 29 and es_biciesto(año):
            return True
        elif mes == 2 and dia < 29:
            return True
        elif dia < 31 and mes in MESES_DE_30:
            return True
        else:
            return False
    else:
        return False
def dias_faltantes_mes(dia, mes, año):
    MESES_DE_31 = [1, 3, 5, 7, 8, 10, 12]
    MESES_DE_30 = [4, 6, 9, 11]
    if mes in MESES_DE_30 and validar_fecha(dia, mes, año):
        return 30 - dia
    elif mes in MESES_DE_31 and validar_fecha(dia, mes, año):
        return 31 - dia
    elif mes == 2 and validar_fecha(dia, mes, año) and es_biciesto(año):
        return 29 - dia
    elif mes == 2 and validar_fecha(dia, mes, año):
        return 28 - dia
    else:
        return "fecha inexistente"
def dias_faltantes_año(dia, mes, año):
    MESES_DICCIONARIO = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
    dias_actuales = 0
    if validar_fecha(dia, mes, año) and es_biciesto(año):
        for recorrido in range(1, mes + 1):
            dias_actuales += MESES_DICCIONARIO[recorrido]
        dias_actuales = dias_actuales - (MESES_DICCIONARIO[mes] - dia)
        dias_actuales += 1
        dias_faltantes = 366 - dias_actuales
    elif validar_fecha(dia, mes, año):
        for recorrido in range(1, mes + 1):
            dias_actuales += MESES_DICCIONARIO[recorrido]
        dias_actuales = dias_actuales - (MESES_DICCIONARIO[mes] - dia)
        dias_faltantes = 365 - dias_actuales
    else:
        return "Fecha inexistente"
    return dias_faltantes
def dias_trascurridos_mes(dia, mes, año):
    MESES_DICCIONARIO = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
    dias_actuales = 0
    if validar_fecha(dia, mes, año) and es_biciesto(año):
        for recorrido in range(1, mes + 1):
            dias_actuales += MESES_DICCIONARIO[recorrido]
        dias_actuales += 1
        dias_actuales = dias_actuales - (MESES_DICCIONARIO[mes] - dia)
    elif validar_fecha(dia, mes, año):
        for recorrido in range(1, mes + 1):
            dias_actuales += MESES_DICCIONARIO[recorrido]
        dias_actuales = dias_actuales - (MESES_DICCIONARIO[mes] - dia)
    else:
        return "Fecha inexistente"
    return dias_actuales
def dias_trasncurridos_años(dia1, mes1, año1, dia2, mes2, año2):
    dias_de_rango_años = 0
    if validar_fecha(dia1, mes1, año1) and validar_fecha(dia2, mes2, año2):
        for años in range(año1 + 1, año2 - 1):
            dias_de_rango_años += 365
            if es_biciesto(años):
                dias_de_rango_años += 1
        if es_biciesto(año1):
            dias_para_terminar_el_año1 = 366 - dias_trascurridos_mes(dia1, mes1, año1)
        else:
            dias_para_terminar_el_año1 = 365 - dias_trascurridos_mes(dia1, mes1, año1)
        if es_biciesto(año2): 
            dias_trasncurridos_en_el_año2 = 366 - dias_trascurridos_mes(dia2, mes2, año2)
        else:
            dias_trasncurridos_en_el_año2 = 365 - dias_trascurridos_mes(dia2, mes2, año2)
        dias_transcurridos = dias_de_rango_años + dias_para_terminar_el_año1 + dias_trasncurridos_en_el_año2
        return dias_transcurridos
    else:
        return "Fecha Inexistente"
def identificar_dia_de_la_semana(dia):
    dias_de_la_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    encendido = True
    while encendido:
        if dia <= 7:
            encendido = False
        elif dia > 7:
            dia = dia - 7
    return dias_de_la_semana[dia - 1]
def pasar_anio_a_romano(anio):
    print("Ejercicio 4.7")
def programa_signo_zodiacal():
    dia = int(input("Ingrese Su Dia De Nacimiento:\n"))
    mes = int(input("Ingrese Su Mes De Nacimiento:\n"))
    if (dia >= 22 and dia <= 31 and mes == 12) or (dia >= 1 and dia <= 20 and mes == 1):
        print("Su Signo Zodiacal Es:\nCapricornio")
    elif (dia >= 21 and dia <= 31 and mes == 1) or (dia >= 1 and dia <= 19 and mes == 2):
        print("Su Signo Zodiacal Es:\nAcuario")
    elif (dia >= 20 and dia <= 29 and mes == 2) or (dia >= 1 and dia <= 20 and mes == 3):
        print("Su Signo Zodiacal Es:\nPiscis")
    elif (dia >= 21 and dia <= 31 and mes == 3) or (dia >= 1 and dia <= 20 and mes == 4):
        print("Su Signo Zodiacal Es:\nAries")
    elif (dia >= 21 and dia <= 30 and mes == 4) or (dia >= 1 and dia <= 20 and mes == 5):
        print("Su Signo Zodiacal Es:\nTauro")
    elif (dia >= 21 and dia <= 31 and mes == 5) or (dia >= 1 and dia <= 20 and mes == 6):
        print("Su Signo Zodiacal Es:\nGeminis")
    elif (dia >= 22 and dia <= 30 and mes == 6) or (dia >= 1 and dia <= 23 and mes == 7):
        print("Su Signo Zodiacal Es:\nCancer")
    elif (dia >= 24 and dia <= 31 and mes == 7) or (dia >= 1 and dia <= 23 and mes == 8):
        print("Su Signo Zodiacal Es:\nLeo")
    elif (dia >= 22 and dia <= 31 and mes == 8) or (dia >= 1 and dia <= 20 and mes == 9):
        print("Su Signo Zodiacal Es:\nVirgo")
    elif (dia >= 24 and dia <= 30 and mes == 9) or (dia >= 1 and dia <= 22 and mes == 10):
        print("Su Signo Zodiacal Es:\nLibra")
    elif (dia >= 23 and dia <= 31 and mes == 10) or (dia >= 1 and dia <= 22 and mes == 11):
        print("Su Signo Zodiacal Es:\nEscorpio")
    elif (dia >= 23 and dia <= 30 and mes == 11) or (dia >= 1 and dia <= 21 and mes == 12):
        print("Su Signo Zodiacal Es:\nSagitario")
    else:
        print("Fecha Inexistente/Signo Inexistente")
def programa_promedio():
    cantidad_de_notas = 0
    nota_final = 0
    while True:
        nota = float(input("INGRESE UNA NOTA: \n"))
        cantidad_de_notas += 1
        nota_final += nota
        mas_notas = int(input("DESEA INGRESAR MAS NOTAS?\n1. SI\n2. NO\n"))
        if mas_notas == -1:
            continue
        elif mas_notas == 2:
            break
    print(nota_final / cantidad_de_notas)
def es_primo(num):
    primo = []
    for x in range(2, num):
        if num % x != 0:
            primo.append(0)
        elif num % x == 0:
            primo.append(1)
    return sum(primo) == 0
def descompocicion_primo(entero):
    numeros_primos = []
    contador = 0
    factores_primos = []
    for x in range(2, entero + 1):
        if es_primo(x):
            numeros_primos.append(x)
    while True:
        if entero % numeros_primos[contador] == 0:
            entero = entero / numeros_primos[contador]
            factores_primos.append(numeros_primos[contador])
        elif entero % numeros_primos[contador] != 0:
            contador += 1
        if entero in numeros_primos:
            break
    print(factores_primos)
def programa_contrasenia():
    contrasenia_inventada = "CHAP"
    contador = 0
    while contador < 3:
        contador += 1
        contrasenia_ingresada = input("Ingrese La contrasenia\n")
        sleep(1)
        if contrasenia_inventada == contrasenia_ingresada:
            return True
    return False
def programa_numero_secreto():
    num1 = randrange(1, 11)
    while True:
        num2 = int(input("Ingrese un numero\n"))
        if num2 < num1:
            print("El numero secreto es mayor")
        elif num2 > num1:
            print("El numero secreto es menor")
        elif num1 == num2:
            print("Los numeros COINCIDEN!")
def algoritmo_de_ulices(n1, m1):
    if m1 % n1 == 0:
        return n1 
    return algoritmo_de_ulices(m1 % n1, n1)
def invertir_cadena_chap(cadena):
    largo = len(cadena) - 1
    cadena_final = ""
    for i in range(len(cadena)):
        cadena_final = cadena_final + cadena[largo - i]
    return cadena_final
def es_potencia_de_2(num):
    while num >= 2:
        num = num / 2
        if num == 2:
            return True
    return False
def suma_de_potencias_de_2(n, m):
    suma = 0
    for x in range(n, m + 1):
        if es_potencia_de_2(x):
            suma += x
    return suma
def suma_de_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma
def numero_perfectos():
    suma = 0
    numeros = []
    for i in range(6, 9000, 2):
        suma = suma_de_divisores(i)
        if suma == i:
            numeros.append(suma)
    return numeros
def numeros_amigos():
    b = 0
    numeros = []
    for a in range(6, 9000, 2):
        b = a
        if suma_de_divisores(a) == b and suma_de_divisores(b) == a:
            numeros.append(a, b)
    return numeros
def programa_suma_de_numeros():
    cantidad_de_numeros = 0
    suma_de_numeros = 0
    while True:
        numero = float(input("Ingrese un numero o Ingrese -1 para salir.\n"))
        if numero == -1.0:
            break
        else:
            suma_de_numeros += numero
            cantidad_de_numeros += 1
    print(f"NUMEROS INGRESADOS: {cantidad_de_numeros}\nSUMA TOTAL: {suma_de_numeros}\nPROMEDIO: {suma_de_numeros / cantidad_de_numeros} ")
def multiplos_dentro_del_segundo_for(a, b):
    numeros_dentro = []
    for x in range(1, b):
        if a * x < b:
            numeros_dentro.append(a * x)
    return numeros_dentro
def multiplos_dentro_del_segundo_while(a, b):
    numeros_dentro = []
    valor_de_iteracion = 1
    while a * valor_de_iteracion < b:
        numeros_dentro.append(a * valor_de_iteracion)
        valor_de_iteracion += 1
    return numeros_dentro
def rango_primo(numero):
    rango = []
    for x in range(2, numero + 1):
        if es_primo(x):
            rango.append(x)
    return rango
def notacion_decimal(digito, numero):
    decimal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if digito in decimal:
        return True
    return False
def examen_aprobado(cantidad_examen, porcentaje_necesario):
    examen_actual = 0
    while examen_actual < cantidad_examen:
        cantidad_de_ejercicios_bien = int(input("Ingrese la cantidad de ejercicios bien hechos\n"))
        if cantidad_de_ejercicios_bien * 10 >= porcentaje_necesario:
            print(cantidad_de_ejercicios_bien * 10," Aprobado\n")
        else:
            print(cantidad_de_ejercicios_bien * 10, " Desaprobado xd\n")
def imprimir_primeros_2_caracteres(cadena):
    print(cadena[0],cadena[1])
def imprimir_ultimos_3_caracteres(cadena):
    print(cadena[-3],cadena[-2],cadena[-1])
def imprimir_cada_2_caracteres(cadena):
    cadena_final = ""
    for x in range(0, len(cadena), 2):
        cadena_final = cadena_final + cadena[x]
    print(cadena_final)
def imprimir_cadena_inversa(cadena):
    cadena_final = ""
    for x in range(len(cadena)):
        cadena_final = cadena_final + cadena[len(cadena)-x - 1]
    print(cadena_final)
    return cadena_final
def imprimir_cadena_normal_inversa(cadena):
    cadena_final = cadena + imprimir_cadena_inversa(cadena)
    print(cadena_final)
def caracter_cada_caracter(cadena, caracter, maxima_cantidad):
    cadena_final = ""
    cantidad = -1
    for x in cadena:
        cadena_final = cadena_final + x + caracter
        cantidad += 1
        if cantidad >= maxima_cantidad:
            break
    cadena_final = cadena_final[0 :-1]
    return cadena_final
def espacio_por_caracter(cadena, caracter, maxima_cantidad):
    cadena_final = ""
    cantidad = 0
    for x in cadena:
        cadena_final = cadena_final + x
        if x == " ":
            cantidad += 1
            cadena_final = cadena_final[0: -1]
            cadena_final = cadena_final + caracter
            if cantidad == maxima_cantidad:
                break
    return cadena_final
def remplazar_digitos_por_caracter(cadena, caracter, maxima_cantidad):
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    cadena_final = ""
    cantidad = 0
    for x in cadena:
        cadena_final = cadena_final + x
        if x in numeros:
            cantidad += 1
            cadena_final = cadena_final[0 : -1]
            cadena_final = cadena_final + caracter
            if cantidad == maxima_cantidad:
                break
    return cadena_final
def insertar_caracter_cada_3_caracters(cadena, caracter, maxima_cantidad):
    cadena_final = ""
    caracter_actual = 0
    for x in cadena:
        cadena_final = cadena_final + x
        caracter_actual += 1
        if caracter_actual % 3 == 0:
            cadena_final = cadena_final + caracter
    if cadena_final[-1] == ".":
        cadena_final = cadena_final[0: -1]
    return cadena_final
def separacion_por_miles(cadena_numerica):
    cadena_final = ""
    nueva_cadena = ""
    caracter_retirados = ""
    cantidad = 0
    if len(cadena_numerica) % 3 == 0:
        nueva_cadena = cadena_numerica
    elif len(cadena_numerica) % 3 == 1:
        nueva_cadena = cadena_numerica[1:]
        caracter_retirados = cadena_numerica[0] + "."
    elif len(cadena_numerica) % 3 == 2:
        nueva_cadena = cadena_numerica[2:]
        caracter_retirados = cadena_numerica[0: 2] + "."
    for x in nueva_cadena:
        cadena_final = cadena_final + x
        cantidad += 1   
        if cantidad % 3 == 0:
            cadena_final = cadena_final + "."
    if cadena_final[-1] == ".":
        cadena_final = cadena_final[0: -1]
    return caracter_retirados + cadena_final
def cada_primer_letra(cadena):
    cadena_final = cadena[0]
    for x in range(0, len(cadena)):
        if cadena[x] == " ":
            cadena_final = cadena_final + cadena[x + 1]
    return cadena_final
def cada_primer_letra_mayuscula(cadena):
    letras_minusculas_a_mayusculas = {"a" : "A", "b" : "B", "c" : "C", "d" : "D", "e" : "E", "f" : "F", "g" : "G",
    "h" : "H", "i" : "I", "j" : "J", "k" : "K", "l" : "L", "m" : "M", "n" : "N", "o" : "O", "v" : "V", "s" : "S", "r" : "R",
    "u" : "U", "y" : "Y", "w" : "W", "x" : "X", "z" : "Z", "p" : "P", "q" : "Q", "0" : "0", "1": "1", "2": "2", "3":"3",
     "4":"4", "5":"5", "6" : "6", "7" : "7", "8" : "8", "9" : "9"}
    letras_mayusculas = ["A","B","C","D", "E","F", "G", "H","I", "J","K", "L", "M", "N","O", "V", "S", "R", "U", "P", "Q"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8" ,"9"]
    cadena_final = ""
    indices = []
    contador = 0
    ultima_cadena = ""
    contador_de_numeros = 0
    for x in range(0, len(cadena)):
        if x == 0:
            cadena_final = cadena_final + letras_minusculas_a_mayusculas[cadena[x]]
        cadena_final = cadena_final + cadena[x]
        if cadena[x] == " ":
            cadena_final = cadena_final + letras_minusculas_a_mayusculas[cadena[x + 1]]
        if cadena[x] in numeros and contador_de_numeros == 0:
            cadena_final = cadena_final[0:-1]
            contador_de_numeros += 1
    cadena_final = list(cadena_final)
    for y in range(0, len(cadena_final)):
        if cadena_final[y] in letras_mayusculas:
            indices.append(y + 1)
    for k in range(len(indices)):
        indices[k] = indices[k] - contador
        contador += 1
    for w in indices:
        cadena_final.pop(w)
    for u in cadena_final:
        ultima_cadena = ultima_cadena + u
    return ultima_cadena

def solo_palabras_con_a(cadena):
    cadena_final = ""
    ultima_cadena = ""
    itereacion_palabra = -1
    contador = -1
    for x in range(len(cadena)):
        if cadena[x] == "a" or cadena[x] == "A":
            if contador == itereacion_palabra:
                itereacion_palabra = x
            while True:
                if itereacion_palabra >= len(cadena) - 1 or cadena[itereacion_palabra] == " ":
                    break
                itereacion_palabra += 1
                contador += 1
                cadena_final += cadena[itereacion_palabra]

    for y in range(len(cadena_final)):
        ultima_cadena += cadena_final[y]
        if cadena_final[y] == "a" or cadena_final[y] == "A":
            ultima_cadena += " "

    return cadena_final
def profe_funcion_letras_con_a(cadena):
    a = ["a", "A"]
    cadena_final = ""
    aux = 0
    for letra in range(len(cadena)):
        if (cadena[letra] in a) and (letra >= aux):
            print(aux, letra)
            aux = letra            
            while True:
                cadena_final += cadena[aux]
                print(aux)
                if (cadena[aux] == " ") or (aux == len(cadena) - 1):
                    break 
                aux += 1
    return cadena_final
def main():
    cadena = "antes del amanecer ayer en el mundial del 2014 messi gano en andorra"
    print(profe_funcion_letras_con_a(cadena))
    print(cadena[12]) 
    print(cadena[18])
main()