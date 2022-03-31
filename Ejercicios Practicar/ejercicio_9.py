# Ejercicio 9 - Nicolas Zwenger

# Realizar una calculadora con operaciones básicas. 
# Se debe validar que el usuario siempre ingrese valores numéricos.

# Impresión de menú de opciones 
print("Bienvenido!")
print("1.- SUMA")
print("2.- RESTA")
print("3.- MULTIPLICACIÓN")
print("4.- DIVISION")
print("5.- EXPONENTE")
print("6.- MODULO")
print("7.- DIVISION ENTERA")

# Entrada de datos según el menú de opciones y comprueba que se ingresen valores númericos 
try:
    operacion = int(input("¿Que operación desearia realizar? Elija del 1 al 7: "))
except ValueError:
    print("Error")
    print("Por favor, ingrese un número")


# Bucle en el que se realizan las operaciones y se controlan si son valores númericos 
while True:
    if operacion < 1 or operacion > 7: # Condicional para controlar que se elija un número entre 1 y 7 según el menú 
        print("Error")
        print("Por favor, ingrese el número correcto")
        break
    try: # Se controla si son valores númericos
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error")
        print("Por favor, ingrese un número")
        break

    # Operaciones aritméticas de la calculadora 
    if operacion == 1:
        print("El resultado es:", num1 + num2)

    elif operacion == 2:
        print("El resultado es:", num1 - num2)

    elif operacion == 3:
        print("El resultado es:", num1 * num2)

    elif operacion == 4:
        print("El resultado es:", num1 / num2)

    elif operacion == 5:
        print("El resultado es:", num1 ** num2)

    elif operacion == 6:
        print("El resultado es:", num1 % num2)

    elif operacion == 7:
        print("El resultado es:", num1 // num2)
    
    break

