import re
from constructores.Constructores import crearUsuarios, crearAuto
from controller.UsuarioControllers import insertarUsuario, user
from data.Usuarios import _usuariosRegistrados
from data.Autos import menuModificarKmAutos, printAutos, menuModificarKmAutos, menuAgregarDetallesAutos, menuModificarPreciosAutos
from data.Bicicletas import printBicicletas, menuAgregarDetallesBicicletas, menuModificarPreciosBicicletas
from data.Camionetas import printCamionetas, menuModificarKmCamionetas, menuAgregarDetallesCamionetas, menuModificarPreciosCamionetas
from data.Motos import printMotos, menuModificarKmMotos, menuAgregarDetallesMotos, menuModificarPreciosMotos
from data.Colectivos import printColectivos, menuModificarKmColectivos, menuAgregarDetallesColectivos, menuModificarPreciosColectivos
from data.Camiones import printCamiones, menuModificarKmCamiones, menuAgregarDetallesCamiones, menuModificarPreciosCamiones
from data.Acoplados import printAcoplados, menuAgregarDetallesAcoplados, menuModificarPreciosAcoplados


def bienvenida():
    print('Bienvenidos a Concesionaria "Rayo McQueen"'.center(1000))
    crearUsuarios()
    crearAuto()

def msjUsuario():
    email = input('Ingrese Correo Electronico: ')
    return email

def msjErrorUsuario():
    print('Usuario Incorrecto')

def msjPassword():
    return input('Ingrese Password: ')

def msjErrorPassword():
    print('Password Incorrecta')


def nivelUsuario():
    if user.nivelUsu == 1:
        menuEmpleado()
    elif user.nivelUsu == 2:
        menuAdmin()

def menuInvitado():
    opcionInv = int(input("1. Ver Vehiculos \n2. Salir \n"))
    if opcionInv == 1:
        print("\n")
        menuVehiculos()
    elif opcionInv == 2:
        print("Hasta luego!")

def menuEmpleado():
    opcionEmp = int(input("1. Ver Vehiculos \n2. Modificar km \n3. Agregar detalles \n4. Salir \n"))
    if opcionEmp == 1:
        print("\n")
        menuVehiculos()
    elif opcionEmp == 2:
        menuModificarKm()
    elif opcionEmp == 3:
        menuAgregarDetalles()
    elif opcionEmp == 4:
        print("Hasta luego!")

def menuAdmin():
    opcionAdm = int(input("1. Ver Vehiculos \n2. Modificar km \n3. Agregar detalles \n4. Modificar precios \n5. Crear nuevos usuarios \n6. Salir \n"))
    if opcionAdm  == 1:
        print("\n")
        menuVehiculos()
    elif opcionAdm  == 2:
        menuModificarKm()
    elif opcionAdm  == 3:
        menuAgregarDetalles()
    elif opcionAdm == 4:
        menuModificarPrecios()
    elif opcionAdm == 5:
        insertarUsuario()
        print(_usuariosRegistrados)
    elif opcionAdm == 6:
        print("Hasta luego!")


def menuVehiculos():
    opcionVeh = int(input("1. Autos \n2. Camionetas \n3. Motos \n4. Bicicletas \n5. Camiones \n6. Acoplados \n7. Colectivos \n"))
    if opcionVeh == 1:
        printAutos()
    elif opcionVeh == 2:
        printCamionetas()
    elif opcionVeh == 3:
        printMotos()
    elif opcionVeh == 4:
        printBicicletas()
    elif opcionVeh == 5:
        printCamiones()
    elif opcionVeh == 6:
        printAcoplados()
    elif opcionVeh == 7:
        printColectivos()


def menuModificarKm():
    opcionVeh = int(input("1. Autos \n2. Camionetas \n3. Motos \n4. Bicicletas \n5. Camiones \n6. Acoplados \n7. Colectivos \n"))
    if opcionVeh == 1:
        printAutos()
        menuModificarKmAutos()
    elif opcionVeh == 2:
        printCamionetas()
        menuModificarKmCamionetas()
    elif opcionVeh == 3:
        printMotos()
        menuModificarKmMotos()
    elif opcionVeh == 4:
        print("Las bicicletas no tienen opción de kilometraje")
    elif opcionVeh == 5:
        printCamiones()
        menuModificarKmCamiones()
    elif opcionVeh == 6:
        print("Los acoplados no tienen opción de kilometraje")
    elif opcionVeh == 7:
        printColectivos()
        menuModificarKmColectivos()

def menuAgregarDetalles():
    opcionVeh = int(input("1. Autos \n2. Camionetas \n3. Motos \n4. Bicicletas \n5. Camiones \n6. Acoplados \n7. Colectivos \n"))
    if opcionVeh == 1:
        printAutos()
        menuAgregarDetallesAutos()
    elif opcionVeh == 2:
        printCamionetas()
        menuAgregarDetallesCamionetas()
    elif opcionVeh == 3:
        printMotos()
        menuAgregarDetallesMotos()
    elif opcionVeh == 4:
        printBicicletas()
        menuAgregarDetallesBicicletas()
    elif opcionVeh == 5:
        printCamiones()
        menuAgregarDetallesCamiones()
    elif opcionVeh == 6:
        printAcoplados()
        menuAgregarDetallesAcoplados()
    elif opcionVeh == 7:
        printColectivos()
        menuAgregarDetallesColectivos()

def menuModificarPrecios():
    opcionVeh = int(input("1. Autos \n2. Camionetas \n3. Motos \n4. Bicicletas \n5. Camiones \n6. Acoplados \n7. Colectivos \n"))
    if opcionVeh == 1:
        printAutos()
        menuModificarPreciosAutos()
    elif opcionVeh == 2:
        printCamionetas()
        menuModificarPreciosCamionetas()
    elif opcionVeh == 3:
        printMotos()
        menuModificarPreciosMotos()
    elif opcionVeh == 4:
        menuModificarPreciosBicicletas()
    elif opcionVeh == 5:
        printCamiones()
        menuModificarPreciosCamiones()
    elif opcionVeh == 6:
        menuModificarPreciosAcoplados()
    elif opcionVeh == 7:
        printColectivos()
        menuModificarPreciosColectivos()
