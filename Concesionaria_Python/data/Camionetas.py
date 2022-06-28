from model.Camioneta import Camioneta

_camionetas = []

def crearCamioneta():
    camioneta = Camioneta('Camioneta 1','Toyota', 'Hilux Dx Dc 4x4', 10000, 'Casi nueva', '33500')
    camioneta_2 = Camioneta('Camioneta 2 ','Ford', 'Ranger 3.2', 63000, 'Impecable', '25000')
    camioneta_3 = Camioneta('Camioneta 3 ','Dodge', 'RAM 1500 Laramie', 0, 'Nueva', '70000')
    camioneta_4 = Camioneta('Camioneta 4 ','Ford', 'F-150 Raptor', 12000, 'Muy poco uso', '115000')
    agregaCamionetas(camioneta, camioneta_2, camioneta_3, camioneta_4)


def agregaCamionetas(camioneta, camioneta_2, camioneta_3, camioneta_4):
    _camionetas.extend([camioneta, camioneta_2, camioneta_3, camioneta_4])


def printCamionetas():
    for camioneta in _camionetas:
        print(camioneta)

def menuModificarKmCamionetas():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    camionetas = _camionetas[pregunta_vehiculo]
    print(camionetas)
    camionetas.km = int(input("Ingrese los kilometros: "))
    printCamionetas()

def menuAgregarDetallesCamionetas():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    camionetas = _camionetas[pregunta_vehiculo]
    print(camionetas)
    camionetas.detalles = camionetas.detalles + ' ' + input("Ingrese los detalles que desea agregar: ")
    printCamionetas()


def menuModificarPreciosCamionetas():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    camionetas = _camionetas[pregunta_vehiculo]
    print(camionetas)
    camionetas.precio = int(input("Ingrese el nuevo precio: "))
    printCamionetas()

crearCamioneta()
