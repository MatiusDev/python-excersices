# Número positivo, negativo o cero
# Solicita un número y muestra si es positivo, negativo o igual a cero.

num = input("Ingrese un número: ").strip()

def validate_number(num):
    if len(num) == 0:
        print("Debe ingresar un valor")
        return False

    try:
        int(num)
        return True
    except ValueError:
        print("Debe ingresar un número valido")
        return False

if (validate_number(num)):
    num = int(num)
    if num < 0:
        print("Es un número negativo")
    elif num == 0:
        print("El número es igual a cero")
    else:
        print("Es un número positivo")

