# Ejercicio 4 - Nicolas Zwenger

# Escriba un programa que pida dos números y luego muestre si el primero es divisible por el segundo.


# Se pregunta al usuario por los dos números.
num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))


divisible = num_1 % num_2 # Fórmula 

# Condicional para comprobar si el primer numero es divisible por el segundo.
if divisible == 0:
    print(f"{num_1} es divisible por {num_2}")
else:
    print("Los números no son divisibles entre si.")