class Colectivo():

    def __init__(self, producto ,marca, modelo, km, detalles, precio):
            self.producto = producto
            self.marca = marca
            self.modelo = modelo
            self.km = km
            self.detalles = detalles
            self.precio = precio

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return f"\nProducto: {self.producto} \nMarca: {self.marca} \nModelo: {self.modelo} \nKilometros: {self.km} \nDetalles: {self.detalles} \nPrecio: {self.precio}"

