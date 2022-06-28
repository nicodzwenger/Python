from model.Colectivo import Colectivo

_colectivos = []

def crearColectivo():
    colectivo = Colectivo('Colectivo 1','Volvo', 'B270F', 130000, 'Muy bien cuidado', '82500')
    colectivo_2 = Colectivo('Colectivo 2 ','Scania', 'Marcopolo G6 K420', 0, 'Nuevo', '45000')
    colectivo_3 = Colectivo('Colectivo 3 ','Mercedes-Benz', 'G7 O500', 800000, 'Muy buen estado', '120000')
    agregaColectivos(colectivo, colectivo_2, colectivo_3)


def agregaColectivos(colectivo, colectivo_2, colectivo_3):
    _colectivos.extend([colectivo, colectivo_2, colectivo_3])


def printColectivos():
    for colectivo in _colectivos:
        print(colectivo)

def menuModificarKmColectivos():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    colectivos = _colectivos[pregunta_vehiculo]
    print(colectivos)
    colectivos.km = int(input("Ingrese los kilometros: "))
    printColectivos()

def menuAgregarDetallesColectivos():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    colectivos = _colectivos[pregunta_vehiculo]
    print(colectivos)
    colectivos.detalles = colectivos.detalles + ' ' + input("Ingrese los detalles que desea agregar: ")
    printColectivos()

def menuModificarPreciosColectivos():
    pregunta_vehiculo = int(input("Ingrese el número del vehiculo: "))
    pregunta_vehiculo = pregunta_vehiculo - 1
    colectivos = _colectivos[pregunta_vehiculo]
    print(colectivos)
    colectivos.precio = int(input("Ingrese el nuevo precio: "))
    printColectivos()


crearColectivo()
