# Ejercicio 7 - Nicolas Zwenger

# Que se le pida al usuario el nombre, la edad, el dinero que hay en su billetera 
# y el hambre que tiene (medido de 0 a 10). Luego que muestre el mensaje:

# Si es menor de 35: Hola - nombre -. Eres una persona joven ya que tu edad es - edad.

# Si es mayor a 34 y tiene más de $500 y su hambre es mayor a 5: Hola - nombre – apellido- ¿Hoy hay asado?

# Si su hambre es de al menos 7 o tiene menos de $100 y su edad es menor a 18: 
# Hola - nombre – apellido - ¿Vas a comer a lo de tus padres?

# Entrada de datos 
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
dinero = int(input("Ingrese cuanto dinero tiene: "))
hambre = int(input("Ingrese cuanto hambre tiene (0-10): "))


# Condicionales que imprimen lo pedido según las condiciones dadas 
if edad < 35:
    print(f"Hola {nombre} eres una persona joven ya que tu edad es {edad}")

if edad > 34 and dinero > 500 and hambre > 5:
    print(f"Hola {nombre} {apellido} ¿Hoy hay asado?")

if edad < 18 and hambre >= 7 or dinero < 100:
    print(f"Hola {nombre} {apellido} ¿Vas a comer a lo de tus padres?")

