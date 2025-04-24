# Aprobado o reprobado
# Pide una nota del 0 al 100. Si es 60 o más, muestra “Aprobado”; si es menor, “Reprobado”.

note = input("Ingrese su nota: ").strip()

def validate_note(note):
    if len(note) == 0:
        print("Debe ingresar un valor válido")
        return False

    try:
        int_note = int(note)

        if int_note < 0 or int_note > 100:
            print("La nota debe estar entre 0 y 100")
            return False
        return True
    except ValueError:
        print("Debe ingresar una nota valida")
        return False

if (validate_note(note)):
    note = int(note)
    if note >= 60:
        print("Aprobado")
    else:
        print("Reprobado")

