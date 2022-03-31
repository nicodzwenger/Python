# Ejercicio 8 - Nicolas Zwenger

# Escriba un programa que solicite el apellido, nombre, año de nacimiento y contraseña. 
# Con las siguientes validaciones:

# El nombre y apellido debe tener al menos 3 vocales.
# El año de nacimiento debe ser un formato correcto: contener solo números y cuatro dígitos.
# La contraseña tiene que tener como mínimo 8 caracteres y un máximo de 16.
# La contraseña al menos debe contener un carácter especial: ! “ # $ % & . -

# Una vez ingresado correctamente todos los valores. Se debe saludar al usuario con su nombre y apellido.


class validaciones():

    # Entrada de datos 
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    nacimiento = input("Ingrese su año de nacimiento: ")
    contraseña = input("Ingrese su contraseña: ")
    print("-------------------------------")

    # Función para controlar que el nombre tenga 3 vocales
    def name(nombre):
        val = True
        conteo = 0
        vocales = set("aeiouAEIOU")
        for i in nombre:
            if i in vocales:
                conteo = conteo + 1

        if conteo < 3:
            print("El nombre debe tener 3 vocales")
            print("-------------------------------")
            val = False

        if val:
            return val

    # Función para controlar que el apellido tenga 3 vocales 
    def last_name(apellido):
        val = True
        conteo = 0
        vocales = set("aeiouAEIOU")
        for abecedario in apellido:

            if abecedario in vocales:
                conteo = conteo + 1

        if conteo < 3:
            print("El apellido debe tener 3 vocales")
            print("-------------------------------")
            val = False

        if val:
            return val

    
    # Función que controla que el año de nacimiento sean números y tenga 4 dígitos 
    def birthday_year(nacimiento):
        val = True

        if not nacimiento.isdigit():
            print("El formato de la fecha de nacimiento debe ser de numeros")
            print("-------------------------------")
            val = False

        if len(nacimiento) != 4:
            print("La fecha de nacimiento debe tener 4 dígitos")
            print("-------------------------------")
            val = False

        if val:
            return val

    # Función que controla que la contraseña tenga un mínimo de 8 cáracteres, máximo de 16 cáracteres y símbolos especiales 
    def password(contraseña):
        simbolos_especiales = ['!', '“', '#', '$', '%', '&', '.', '-']
        val = True

        if len(contraseña) < 8:
            print("La contraseña debe tener al menos 8 cáracteres")
            print("-------------------------------")
            val = False

        if len(contraseña) > 16:
            print("La contraseña debe tener un máximo de 16 cáracteres")
            print("-------------------------------")
            val = False

        if not any(char in simbolos_especiales for char in contraseña):
            print("La contraseña debe tener estos simbolos: '! “ # $ % & . -' ")
            print("-------------------------------")
            val = False
        
        if val:
            return val


    # Condicionales con las llamadas a la función asignadas para que imprima si la entrada de datos es correcta 
    nom = name(nombre)
    if nom == True:
        print("El nombre es correcto")
        print("-------------------------------")

    ape = last_name(apellido)
    if ape == True:
        print("El apellido es correcto")
        print("-------------------------------")

    nac = birthday_year(nacimiento)
    if nac == True:
        print("La fecha es correcta")
        print("-------------------------------")


    con = password(contraseña)
    if con == True:
        print("La contraseña es correcta")
        print("-------------------------------")


    # Condicional que te da la bienvenida si todas las entradas de datos son correctas 
    if nom == True and ape == True and nac == True and con == True:
        print(f"Bienvenido {nombre} {apellido}")