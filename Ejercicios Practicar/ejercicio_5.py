# Ejercicio 5 - Nicolas Zwenger

# Escribe un programa que pida 3 números e imprima el mayor de los tres.


# Entrada de datos
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Condicionales de comprobación para imprimir cual de los 3 números es mayor 
if num1 > num2 and num1 > num3:
    print(f"{num1} es el mayor")
elif num2 > num1 and num2 > num3:
    print(f"{num2} es el mayor")
elif num3 > num1 and num3 > num2:
    print(f"{num3} es el mayor")

# Condicional en caso de que los 3 números sean iguales 
elif num1 == num2 and num1 == num3 and num2 == num1 and num2 == num3 and num3 == num1 and num3 == num2:
    print("Los 3 numeros son iguales.")

# Condicionales que comprueban en caso de que son 2 números sean iguales pero mayor que el tercer número
elif num1 == num2 and num1 != num3:
    print(f"{num1} y {num2} son iguales pero mayores que {num3}")
elif num2 == num3 and num2 != num1:
    print(f"{num2} y {num3} son iguales pero mayores que {num1}")
elif num1 == num3 and num1 != num2:
    print(f"{num1} y {num3} son iguales pero mayores que {num2}")

