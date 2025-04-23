# Suma de dos números
# Solicita dos números al usuario, realiza la suma y muestra el resultado.

# nums = input("Ingrese dos números separados por un espacio: ")
num_1 = input("Ingrese un número: ").strip()
num_2 = input("Ingrese otro número: ").strip()
# num_1, num_2 = nums.split(" ")[:2]

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
    result = int(num_1) + int(num_2)
    print(f"La suma de sus números es {result}")

