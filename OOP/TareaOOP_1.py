# Un concesionario te contrata para realizar un software ya que quiere llevar un control de los automóviles que tiene para vender.
# Se sabe que este concesionario vende: bicicletas, motos, autos, camioneta, colectivos, camiones y acoplados.
# Realizar las clases correspondientes a cada elemento.
# Generar objetos de cada una de las clases.
# Imprimir por terminal los ejemplos realizados con sus características.
# OPCIONAL: que el usuario ingrese los atributos de los objetos por consola.


class Bicicletas():
    def __init__(self, color, marca, modelo, talla) :
        self.colorBicicleta = color
        self.marcaBicicleta  = marca
        self.modeloBicicleta = modelo
        self.tallaBicicleta = talla

    @classmethod
    def input_usuario(cls):
        return cls(
        input("Ingrese el color de la bicicleta: "),
        input("Ingrese la marca de la bicicleta: "),
        input("Ingrese el modelo de la bicicleta: "),
        input("Ingrese la talla de la bicicleta (XS-XL): ")
        )

miBicicleta = Bicicletas.input_usuario()
print(Bicicletas.self)

#class Motos():

#class Autos():

#class Camionetas():

#class Colectivos():

#class Camiones():

#class Acoplados():
