class Acoplado():

    def __init__(self, producto, marca, detalles, precio):
            self.producto = producto
            self.marca = marca
            self.detalles = detalles
            self.precio = precio

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return f"\nProducto: {self.producto} \nMarca: {self.marca} \nDetalles: {self.detalles} \nPrecio: {self.precio}"
