# Realizar el juego PIEDRA, PAPEL O TIJERA. El usuario deberá competir contra la PC. 
# El triunfador será quien gane 3 partidas.

# Aclaraciones al final.

import random

ganar = 0
perder = 0
empate = 0
usuario = 0
cont = 0

while cont < 3:
    try:
        usuario = int(input("\n1.- Piedra \n2.- Papel \n3.- Tijera \nIngrese que quiere jugar (1/2/3): "))
        cont = cont + 1

    except ValueError:
        print("Error! Ingrese un número por favor.")
        continue

    if usuario < 1 or usuario > 3:
        print("Error, ingrese el número correcto.")
        break

    print("---------------------------------")

    if usuario == 1:
        print("Jugaste Piedra")
    elif usuario == 2:
        print("Jugaste Papel") 
    elif usuario == 3:
        print("Jugaste Tijera")

    print("---------------------------------")

    pc = random.randint(1, 3)
    if pc == 1:
        print("La computadora jugó Piedra")
    elif pc == 2:
        print("La computadora jugó Papel") 
    elif pc == 3:
        print("La computadora jugó Tijera")

    print("---------------------------------")

    if usuario == 1 and pc == 2:
        print("Perdiste!")
        perder += 1
    elif usuario == 1 and pc == 3:
        print("Ganaste!")
        ganar += 1


    elif usuario == 2 and pc == 1:
        print("Ganaste!")
        ganar += 1
    elif usuario == 2 and pc == 3:
        print("Perdiste!")
        perder += 1

    elif usuario == 3 and pc == 2:
        print("Ganaste!")
        ganar += 1
    elif usuario == 3 and pc == 1:
        print("Perdiste!")
        perder += 1

    elif usuario == pc:
        print("Empate!")
        empate += 1

    print("---------------------------------")



if ganar > 2:   
    print("GANASTE EL JUEGO")
elif perder > 2:
    print("PERDISTE EL JUEGO")
elif empate > 2 or empate == ganar or empate == perder:
    print("EMPATARON")


# Cosas a mejorar o que faltan:
# 1.- Asignar un mejor contador del bucle ya que tiene errores

# 2.- Asignar de manera correcta que al final del juego diga que se ganó, empató o perdió
# He tenido problemas en querer asignar demasiados valores en 1 sola variable y no se llegan a sumar hasta los 3 (en ganar y perder)
