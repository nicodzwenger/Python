# Escribir un código que muestre en orden alfabético las palabras ingresadas.

# Aclaraciones al final

lista_palabras = []

palabras = ""

while True:
    palabras = input("Ingrese palabras: ")

    lista_palabras.append(palabras)

    lista_palabras.sort()

    if palabras.lower() == "exit":
        break


lista_palabras.remove("exit")

print(lista_palabras)


# No pude lograr usar el "isalpha()" 
# Ya que no se permite usar con objetos dentro de una lista y no supe como implementarlos desde las string.
