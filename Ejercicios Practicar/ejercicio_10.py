# Ejercicio 10 - Nicolas Zwenger

# Realizar un juego donde el usuario debe adivinar el número arrojado por la función random.
# Solamente cuenta con 5 intentos

import random # Importación del módulo random 


# Impresión del menú del juego con su respectivas reglas 
print("Bienvenido!")
print("El juego consiste en que debes adivinar un número cualquiera entre el 1 y el 50")
print("Tienes 5 intentos para adivinar")
print("Buena suerte!")
print("-----------------------------")

# Bucle que limita los 5 intentos 
for i in reversed(range(5)):
    numero_input = int(input("Ingrese el número: ")) # Entrada de datos 
    numero_random = random.randint(1, 50) # Se almacena el número random entre el rango 1-50 en una variable 
    if numero_input < 1 or numero_input > 50: # Se fija si el rango de los números ingresados es menor o mayor al establecido en las reglas 
        print("Error, el numero debe estar en el rango de 1-50")
        break
    print("El número random era:", numero_random) # Imprime el número random 

    if numero_input == numero_random: # Condicional con mensaje de impresión si se acierta el número 
        print("Felicidades! Acertaste el número!")
        break
    print("-----------------------------")
    print(f"Te quedan {i} intentos") # El bucle es con rango en reversa para poder imprimir los intentos restantes 
    print("-----------------------------")

    if i == 0:
        print("Game Over!") # Mensaje de impresión al quedarse sin intentos 


