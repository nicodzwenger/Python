from model.Acoplado import Acoplado

_acoplados = []

def crearAcoplado():
    acoplado = Acoplado('Acoplado 1','Pratti', 'Viejo', '1700')
    acoplado_2 = Acoplado('Acoplado 2','Lambert', 'Nuevo', '11000')
    acoplado_3 = Acoplado('Acoplado 3','Hermann', 'En buen estado', '2600')
    agregaAcoplados(acoplado, acoplado_2, acoplado_3)


def agregaAcoplados(acoplado, acoplado_2, acoplado_3):
    _acoplados.extend([acoplado, acoplado_2, acoplado_3])


def printAcoplados():
    for acoplado in _acoplados:
        print(acoplado)

def menuAgregarDetallesAcoplados():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    acoplados = _acoplados[pregunta_vehiculo]
    print(acoplados)
    acoplados.detalles = acoplados.detalles + ' ' + input("Ingrese los detalles que desea agregar: ")
    printAcoplados()

def menuModificarPreciosAcoplados():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    acoplados = _acoplados[pregunta_vehiculo]
    print(acoplados)
    acoplados.precio = int(input("Ingrese el nuevo precio: "))
    printAcoplados()

crearAcoplado()