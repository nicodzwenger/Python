# Ejercicio 1 - Nicolas Zwenger

# Desarrollar un programa que le pida al alumno todas las materias que está cursando (al menos 4)
# y luego se le debe pedir las respectivas notas de los 3 parciales de las asignaturas ingresadas. 
# Por último el programa debe calcular el promedio de las evaluaciones y definir por cada una de ellas:

# Si la materia tiene como promedio un 8 o más: Materia promocionada.
# Si la materia tiene como promedio una nota menor a 8 pero mayor o igual a 6: Materia aprobada.
# Si la materia tiene como promedio una nota menor que 6: Materia desaprobada.

# Para que el ejercicio sea válido se deben utilizar listas


lista = [] # Definición de variable con lista vacía 

# Entrada de datos para las materias con bucle para limitar que se ingresen solo 4 materias 
for i in range(4):
    materias = input("Ingrese la materia: ")
    lista.append(materias) # Pasaje de las entradas de tipo string a la lista 


# Conversión de elementos de la lista a strings
materia_1 = lista[0]
materia_2 = lista[1]
materia_3 = lista[2]
materia_4 = lista[3]

# Entrada de datos de las notas de las materias 
for i in range(1):
    nota_materia1 = float(input(f"Introduzca la primer nota de {materia_1}: "))
    nota2_materia1 = float(input(f"Introduzca la segunda nota de {materia_1}: "))
    nota3_materia1 = float(input(f"Introduzca la tercer nota de {materia_1}: "))

    nota_materia2 = float(input(f"Introduzca la primer nota de {materia_2}: "))
    nota2_materia2 = float(input(f"Introduzca la segunda nota de {materia_2}: "))
    nota3_materia2 = float(input(f"Introduzca la tercer nota de {materia_2}: "))

    nota_materia3 = float(input(f"Introduzca la primer nota de {materia_3}: "))
    nota2_materia3 = float(input(f"Introduzca la segunda nota de {materia_3}: "))
    nota3_materia3 = float(input(f"Introduzca la tercer nota de {materia_3}: "))

    nota_materia4 = float(input(f"Introduzca la primer nota de {materia_4}: "))
    nota2_materia4 = float(input(f"Introduzca la segunda nota de {materia_4}: "))
    nota3_materia4 = float(input(f"Introduzca la tercer nota de {materia_4}: "))

    # Promedio de las notas de las materias
    promedioMat1 = (nota_materia1 + nota2_materia1 + nota3_materia1) / 3
    promedioMat2 = (nota_materia2 + nota2_materia2 + nota3_materia2) / 3
    promedioMat3 = (nota_materia3 + nota2_materia3 + nota3_materia3) / 3
    promedioMat4 = (nota_materia4 + nota2_materia4 + nota3_materia4) / 3

    print("--------------------------")

    # Condicionales para separar por promedios e imprimir si se promocionó, aprobó u desaprobó 
    if promedioMat1 >= 8:
        print(f"Promocionaste {materia_1}!")
    elif promedioMat1 < 8 and promedioMat1 >= 6:
        print(f"Aprobaste {materia_1}")
    elif promedioMat1 < 6:
        print(f"Desaprobaste {materia_1}")


    if promedioMat2 >= 8:
        print(f"Promocionaste {materia_2}!")
    elif promedioMat2 < 8 and promedioMat2 >= 6:
        print(f"Aprobaste {materia_2}")
    elif promedioMat2 < 6:
        print(f"Desaprobaste {materia_2}")


    if promedioMat3 >= 8:
        print(f"Promocionaste {materia_3}!")
    elif promedioMat3 < 8 and promedioMat3 >= 6:
        print(f"Aprobaste {materia_3}")
    elif promedioMat3 < 6:
        print(f"Desaprobaste {materia_3}")


    if promedioMat4 >= 8:
        print(f"Promocionaste {materia_4}!")
    elif promedioMat4 < 8 and promedioMat4 >= 6:
        print(f"Aprobaste {materia_4}")
    elif promedioMat4 < 6:
        print(f"Desaprobaste {materia_4}")


# Impresión de los promedios 
print(" ")
print("PROMEDIOS: ")
print(f"Promedio de {materia_1}:", promedioMat1)
print(f"Promedio de {materia_2}:", promedioMat2)
print(f"Promedio de {materia_3}:", promedioMat3)
print(f"Promedio de {materia_4}:", promedioMat4)