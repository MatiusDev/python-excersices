# Edad futura
# Pide al usuario su edad y muestra cuántos años tendrá dentro de 5 años.

age = input("Ingrese un número: ").strip()

def validate_age(age):
    if len(age) == 0:
        print("Debe ingresar un valor")
        return False

    try:
        int(age)
        return True
    except ValueError:
        print("Debe ingresar un número valido")
        return False

if (validate_age(age)):
    future_age = int(age) * 5
    print(f"Dentro de 5 años tendrás {future_age}")

