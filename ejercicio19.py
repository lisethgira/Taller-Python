
A = 0
D = 0

for C in range(1, 37):
    Nom = input("Ingrese el nombre: ")
    Pat = input("Ingrese el apellido paterno: ")
    Mat = input("Ingrese el apellido materno: ")
    N1 = float(input("Ingrese la primera nota: "))
    N2 = float(input("Ingrese la segunda nota: "))

    cod = Pat[:2] + Mat[1:3] + Nom[-2:] + str(C)

    prom = (N1 + N2) / 2

    print(cod, prom)

    if prom >= 10.5:
        A += 1
    else:
        D += 1

print("Aprobados:", A)
print("Desaprobados:", D)