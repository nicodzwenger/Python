class Usuario():

    def __init__(self, nombre, apellido, correo, password, nivelUsu):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
        self.nivelUsu = nivelUsu

    def __repr__(self):
        return str(self.__dict__)

    
    def __str__(self):
        return f'Nombre: {self.nombre}. Apellido: {self.apellido}. Correo: {self.correo}. Password: {self.password}. Nivel Usuario: {self.nivelUsu}' 
