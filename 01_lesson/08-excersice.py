# Mayor de dos números
# Solicita dos números y muestra cuál es el mayor. Si son iguales, indícalo.

num_1 = input("Ingrese un número: ").strip()
num_2 = input("Ingrese otro número: ").strip()

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

if (validate_number(num_1) and validate_number(num_2)):
    if num_1 > num_2:
        print("El primer número es mayor")
    elif num_2 > num_1:
        print("El segundo número es mayor")
    else:
        print("Los números son iguales")

