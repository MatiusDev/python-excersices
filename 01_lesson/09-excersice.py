# Calculadora simple
# Crea una pequeña calculadora que permita al usuario ingresar dos números y una operación (+, -, *, /) y luego muestre el resultado.

def validate_number(num):
    if len(num) == 0:
        print("Debe ingresar un valor")
        return False

    try:
        int(num)
        return True
    except ValueError:
        return False

while(True):
    opt = input("Operaciones aritmeticas" \
    "\n- Ingrese la operación que desea (+, -, *, /)" \
    "\n- Ingrese X para salir\nDigite su opción: ")

    num_1 = input("Ingrese un número: ").strip()
    num_2 = input("Ingrese otro número: ").strip()

    if (not validate_number(num_1) or not validate_number(num_2)):
        print("Por favor ingrese números validos")
        continue
    
    if opt == '+':
        result = int(num_1) + int(num_2)
        print("Los números sumandos son {result}")
    if opt == '-':
        result = int(num_1) - int(num_2)
        print("Los números restados son {result}")
    if opt == '*':
        result = int(num_1) * int(num_2)
        print("Los números multiplicados son {result}")
    if opt == '/':
        num_2 = int(num_2)
        if (num_2 == 0):
            print("Ops! No puedes didivir sobre cero, ¡NO EXISISTE!")
            continue

        result = int(num_1) / num_2
        print("Los números divididos son {result}")

    if opt.upper() == 'X':
        break

# products = []
# p_names = []
# p_prices = []
# p_units = []

# for i in range(0, len(products)):
#     total_value = p_units[i] * p_prices[i]
#     print(f"[{p_names[i]}]: compraste {p_units[i]} unidades y debes pagar: {total_value}")