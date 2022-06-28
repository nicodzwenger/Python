from typing import Type
from ui.Views import bienvenida, msjPassword, msjUsuario, msjErrorPassword, msjErrorUsuario, menuInvitado, nivelUsuario
from controller.UsuarioControllers import buscarUsuario, validarContrasenia
from constructores.Constructores import crearUsuarios

def bienvenida():
    print('Bienvenidos a Concesionaria "Rayo McQueen"'.center(800))
    crearUsuarios()


def preguntaMenu():
    print("***USTED ESTÁ ACTUALMENTE COMO INVITADO***")
    pregunta_menu = input("¿Desea loguear como Empleado o Administrador? (Si/No)\n")

    if pregunta_menu.lower() == "si":
        userOk = buscarUsuario(msjUsuario())
        if(userOk):
            passOk = validarContrasenia(msjPassword())
            if(passOk):
                nivelUsuario()
            else:
                msjErrorPassword()

        else:
            msjErrorUsuario()
    elif pregunta_menu.lower() == "no":
        menuInvitado()
    else:
        print("Respuesta no válida")
 

bienvenida()
preguntaMenu()
