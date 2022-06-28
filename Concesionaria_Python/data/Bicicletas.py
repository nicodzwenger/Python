from model.Bicicleta import Bicicleta

_bicicletas = []

def crearBicicleta():
    bicicleta = Bicicleta('Bicicleta 1','Mountain Bike Silverfox', 'FM18SI29AM211', 'Nueva', '300')
    bicicleta_2 = Bicicleta('Bicicleta 2','Mountain Bike Shifter', 'FM18S6SM210D', 'Nueva', '270')
    bicicleta_3 = Bicicleta('Bicicleta 3 ','BMX', 'TopMega Crossboy R16', 'Nueva', '240')
    bicicleta_4 = Bicicleta('Bicicleta 4 ','Mountain Bike Fierce', 'M18F29AM210','Nueva', '335')
    agregaAutos(bicicleta, bicicleta_2, bicicleta_3, bicicleta_4)


def agregaAutos(bicicleta, bicicleta_2, bicicleta_3, bicicleta_4):
    _bicicletas.extend([bicicleta, bicicleta_2, bicicleta_3, bicicleta_4])


def printBicicletas():
    for bicicleta in _bicicletas:
        print(bicicleta)

def menuAgregarDetallesBicicletas():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    bicicletas = _bicicletas[pregunta_vehiculo]
    print(bicicletas)
    bicicletas.detalles = bicicletas.detalles + ' ' + input("Ingrese los detalles que desea agregar: ")
    printBicicletas()

def menuModificarPreciosBicicletas():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    bicicletas = _bicicletas[pregunta_vehiculo]
    print(bicicletas)
    bicicletas.precio = int(input("Ingrese el nuevo precio: "))
    printBicicletas()

crearBicicleta()
