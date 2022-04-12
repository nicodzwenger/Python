import numpy as np

filas = 10
columnas = 10
fila = 0
columna = 0

arreglo_vacio = np.zeros([filas,columnas])
barcos = np.array([[1,1,1,0,0,0,0,0,0,1],
                    [0,0,1,1,1,0,0,0,0,1],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,1,1,1,1,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0,0,0],
                    [0,0,0,1,0,0,0,1,0,0],
                    [0,0,0,1,0,0,0,1,0,0],
                    [1,1,0,0,0,0,0,1,0,0]])
vidas = 12
arreglo_vacio = barcos
x=0
print("es de 10 x 10 la matriz\n")

while vidas > 0:
    try:
        fila = int(input("Ingresa n° de fila: "))
        columna = int(input("Ingresa n° de columna: "))
    except ValueError:
        print("Ingrese un valor númerico.")
        continue
    try:
        if barcos[fila-1,columna-1] and arreglo_vacio [fila-1,columna-1] == 1:
            print("Me diste!!!")
            arreglo_vacio[fila-1,columna-1]=0
            x +=1
        else:
            print("Ya disparaste en lugar o no hay nada!")
            vidas -=1
            print("te quedan...♥",vidas,"vidas")
        if x == 21:
            vidas = 0
    except:
        print("El valor de las filas y columnas deben ser entre 1-10")

if vidas == 0 and x == 21:
    print("GANASTE")

