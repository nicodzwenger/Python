# Ejercicio 6 - Nicolas Zwenger

# Realizar un programa que pida nombres de amigos hasta que se ingrese “exit”. 
# Luego, se deben mostrar todos los nombres de amigos concatenados con un guion ( - ).


nombres_2 = [] # Definición de variable con lista vacía 
nombres = "" # Definición de variable vacía para inicializar el bucle 


# Bucle para preguntar nombres de amigos al usuario hasta que se ingrese "exit" 
while nombres != "exit":
    nombres = input("Ingrese nombres de amigos: ") # Entrada de datos
    nombres_2.append(nombres) # Conversión de datos tipo string a lista

nombres_2.pop() # Se elimina el último elemento de la lista, en este caso, el "exit" 

nombre_amigos = ' - '.join(nombres_2) # Conversión de lista a string y se concatenan las strings con un guión
print("\nLos nombres de los amigos son:", nombre_amigos) # Salida de datos

