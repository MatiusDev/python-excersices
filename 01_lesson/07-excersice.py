# Par o impar
# Pide un número entero al usuario y muestra si es par o impar.

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
    if (num % 2 == 0):
        print(f"El número {num} es par")
    else:
        print(f"El número {num} es impar")