from model.Auto import Auto

_autos = []

def crearAuto():
    auto = Auto('Auto 1','VW', 'Gol', 15225, 'Muy bonito', '10000')
    auto_2 = Auto('Auto 2 ','Ford', 'Fiesta', 12000, 'En buen estado', '10500')
    auto_3 = Auto('Auto 3 ','Toyota', 'Corolla 2.0', 3000, 'Excelente estado', '30000')
    auto_4 = Auto('Auto 4 ','BMW', 'Serie 8 M850i', 0, 'Nuevo', '272000')
    agregaAutos(auto, auto_2, auto_3, auto_4)


def agregaAutos(auto, auto_2, auto_3, auto_4):
    _autos.extend([auto, auto_2, auto_3, auto_4])


def printAutos():
    for auto in _autos:
        print(auto)

def menuModificarKmAutos():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    autos = _autos[pregunta_vehiculo]
    print(autos)
    autos.km = int(input("Ingrese los kilometros: "))
    printAutos()

def menuAgregarDetallesAutos():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    autos = _autos[pregunta_vehiculo]
    print(autos)
    autos.detalles = autos.detalles + ' ' + input("Ingrese los detalles que desea agregar: ")
    printAutos()

def menuModificarPreciosAutos():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    autos = _autos[pregunta_vehiculo]
    print(autos)
    autos.precio = int(input("Ingrese el nuevo precio: "))
    printAutos()

crearAuto()