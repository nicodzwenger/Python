from data.Usuarios import _usuariosRegistrados, agregaUsuarios
from model.Usuario import Usuario


user = Usuario('', '',
                '', '', '')


def buscarUsuario(correo):
    for usuario in _usuariosRegistrados:
        if usuario.correo == correo:
            user.nombre = usuario.nombre
            user.apellido = usuario.apellido
            user.correo = usuario.correo
            user.password = usuario.password
            user.nivelUsu = usuario.nivelUsu
            return True

def validarContrasenia(password):
    if user.password == str(password):
        print('BIENVENIDO')
        return True


def insertarUsuario():
    respuesta = True
    while respuesta:
        usuario = Usuario(input("Ingrese el nombre del nuevo usuario: "),
        input("Ingrese el apellido del nuevo usuario: "),
        input("Ingrese el correo del nuevo usuario: "),
        input("Ingrese la contraseña del nuevo usuario: "),
        int(input("Ingrese el nivel del usuario del nuevo usuario: ")),
        )
        agregaUsuarios(usuario)
        print("Usuario creado con éxito!")
        pregunta = input("¿Desea crear otro usuario? \n")
        if pregunta == "no":
            return False
        else:
            continue