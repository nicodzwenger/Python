# Desarrollar un software que permita ingresar números. 
# Por cada ingreso se debe mostrar el mayor, menor, el total y el promedio hasta el momento.

numeros = 0
lista = []

while True:
    try:
        numeros = int(input("Ingrese numeros: "))
    except ValueError:
        print("ERROR! Ingrese un número por favor.")
        continue


    try:
        pregunta = input("¿Desea ingresar otro número? ('S' o 'N'): ")
        if pregunta.lower() == "s":
            pass
    
        elif pregunta.lower() == "n":
            print(f"El número mayor es: {mayor}")
            print(f"El número menor es: {menor}")
            print(f"El total es: {total}")
            print(f"El promedio es de: {promedio}")
            print("\n")
            print("Gracias por usar el programa")
            break

        else:
            print("Error, debes ingresar 'S' o 'N'")
            continue

    except Exception:
        print("Error!")



    lista.append(numeros)
    print(lista)
    
    menor = min(lista)
    mayor = max(lista)
    total = sum(lista)
    promedio = sum(lista) / len(lista)


    print(f"El número mayor actual es: {mayor}")
    print(f"El número menor actual es: {menor}")
    print(f"El total actual es: {total}")
    print(f"El promedio actual es de: {promedio}")

