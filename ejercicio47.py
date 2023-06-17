presupuesto = int(input("¿Cual es el presupuesto?"))

areas = [
    (list(["Ginecologia", 40])),
    (list(["Traumatologia", 30])),
    (list(["Pediatria", 30]))
]

for area in areas:
    nombre = area[0]
    porcentage = area[1]

    resultado = presupuesto * (porcentage / 100)

    print(nombre, ": ", resultado)