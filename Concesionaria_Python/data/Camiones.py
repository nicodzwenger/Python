from model.Camion import Camion

_camiones = []

def crearCamion():
    camion = Camion('Camion 1','Iveco', 'Cursor 330', 100000, 'Excelente estado', '65000')
    camion_2 = Camion('Camion 2 ','Volkswagen', 'Constellation', 460000, 'Muy buen estado', '65000')
    camion_3 = Camion('Camion 3 ','Scania', 'G310', 7400, 'Casi nuevo', '100000')
    agregaCamiones(camion, camion_2, camion_3)


def agregaCamiones(camion, camion_2, camion_3):
    _camiones.extend([camion, camion_2, camion_3])


def printCamiones():
    for camion in _camiones:
        print(camion)


def menuModificarKmCamiones():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    camiones = _camiones[pregunta_vehiculo]
    print(camiones)
    camiones.km = int(input("Ingrese los kilometros: "))
    printCamiones()

def menuAgregarDetallesCamiones():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    camiones = _camiones[pregunta_vehiculo]
    print(camiones)
    camiones.detalles = camiones.detalles + ' ' + input("Ingrese los detalles que desea agregar: ")
    printCamiones()


def menuModificarPreciosCamiones():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    camiones = _camiones[pregunta_vehiculo]
    print(camiones)
    camiones.precio = int(input("Ingrese el nuevo precio: "))
    printCamiones()


crearCamion()
