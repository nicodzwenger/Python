from model.Usuario import Usuario
from model.Auto import Auto
from data.Usuarios import agregaUsuarios
from data.Autos import agregaAutos

def crearUsuarios():
    usuario = Usuario('Lionel', 'Messi',
                      'admin@admin.com', 'admin', 2)
    agregaUsuarios(usuario)
    usuario = Usuario('Lewis', 'Hamilton',
                      'empleado@empleado.com', '1', 1)
    agregaUsuarios(usuario)
    usuario = Usuario('John', 'Travolta',
                      'empleado.emp@empleado.com', '1', 1)
    agregaUsuarios(usuario)


def crearAuto():
    auto = Auto('VW', 'Gol', 15225, 'Muy bonito')
    agregaAutos(auto)


