def informarError():
    correo = input('Ingrese su correo: ')
    nombre = input('Ingrese su nombre: ')
    print(
        f'Gracias {nombre}. Cuando solucionemos el problema le enviaremos un correo a {correo}')


def opcionUsuario(params):
    opcionUsuario = int(input(f"Desea {params}?\n Si=0 No=1: "))
    return opcionUsuario


opcion = 0
while opcion == 0:
    try:
        numero = int(input("Ingrese un numero para sumar: "))
        numero2 = int(input("Ingrese otro numero para sumar: "))
        print(numero + numero2)
    except ValueError:
        dato = opcionUsuario("informar el error")
        if(dato == 0):
            informarError()
    else:
        print('Suma realizada con exito')
    finally:
        opcion = opcionUsuario('continuar')

print('Gracias por utilizar la Calculadora')