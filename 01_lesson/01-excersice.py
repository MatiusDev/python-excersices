# Hola Mundo personalizado
# Pide al usuario su nombre y muestra un saludo personalizado en pantalla.

import random

name = input("Ingrese su nombre: ").strip()

def validate_name(name):
    if (len(name) == 0):
        print("El nombre está vacío")
        return False

    name_no_spaces = name.replace(' ', '')
    if (not name_no_spaces.isalpha()):
        print("Su nombre solo debe tener letras")
        return False

    return True

def say_hello(name):
    if (not validate_name(name)):
        return

    greetings = [
        f"Bienvenido {name}, es un placer saludarte",
        f"Es un honor tener aquí {name}",
        f"Saludos terricola {name}",
        f"¿Que haremos hoy? {name}",
        f"Hola mundo! te deseo un gran día {name}",
        f"Tons {name}? Ready o no mi socio",
        f"¿Que hay pa hacer hoy? {name}",
        f"Mi estimado {name}, me complace saludarle el día de hoy.",
        f"Hola {name}!!! ¿cómo te ha ido hoy?"
    ]
    opt = random.randint(0, len(greetings)) 
    print(greetings[opt])

say_hello(name)
