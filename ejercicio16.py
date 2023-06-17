 
horastrabajadas = float(input("Ingrese las horas trabajadas: "))
dia = input("Ingrese el día de la semana: ")
turno = input("Ingrese el turno (diurno/nocturno): ")

while dia != "domingo":
    jornal = 0

    if turno == "diurno":
        jornal = 10 * horastrabajadas
    else:
        jornal = 50 * horastrabajadas

    print("El jornal es:", jornal)

    # Solicitar nueva entrada de datos
    horastrabajadas = float(input("Ingrese las horas trabajadas: "))
    dia = input("Ingrese el día de la semana: ")
    turno = input("Ingrese el turno (diurno/nocturno): ")

if horastrabajadas < 15:
    print("Trabajador en observación")
else:
    print("El jornal mensual es:", jornal)