from model.Moto import Moto

_motos = []

def crearMoto():
    moto = Moto('Moto 1','Honda', 'Wave 110', 0, 'Nueva', '1350')
    moto_2 = Moto('Moto 2 ','Motomel', 'Blitz 110', 3000, 'Casi nueva', '730')
    moto_3 = Moto('Moto 3 ','Jawa', 'Daytona 350', 13500, 'Bien cuidada', '3100')
    moto_4 = Moto('Moto 4 ','Kawasaki', 'Ninja 400', 0, 'Nueva', '13000')
    agregaMotos(moto, moto_2, moto_3, moto_4)


def agregaMotos(moto, moto_2, moto_3, moto_4):
    _motos.extend([moto, moto_2, moto_3, moto_4])


def printMotos():
    for moto in _motos:
        print(moto)

def menuModificarKmMotos():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    motos = _motos[pregunta_vehiculo]
    print(motos)
    motos.km = int(input("Ingrese los kilometros: "))
    printMotos()

def menuAgregarDetallesMotos():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    motos = _motos[pregunta_vehiculo]
    print(motos)
    motos.detalles = motos.detalles + ' ' + input("Ingrese los detalles que desea agregar: ")
    printMotos()

def menuModificarPreciosMotos():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    motos = _motos[pregunta_vehiculo]
    print(motos)
    motos.precio = int(input("Ingrese el nuevo precio: "))
    printMotos()


crearMoto()
