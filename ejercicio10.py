ti = input("introduzca el tiempo: ")
di = input("introduzca el dia: ")
tu= input("introduzca el turno: ")

ti = int(ti)
di = int(di)
tu = int(tu)

if ti < 5:
    pag =ti * 1
else:
    if ti < 8:
        pag = ( ti - 5) * 0.8 + 5
    else:
        if ti <= 10:
            pag =(ti - 8) * 0.7 + 7.4
        else:
            pag = (ti - 10) * 0.5 + 8.8

if di == "domingo":
    im = pag * 0.05
else:
    if tu == "m":
        im = pag * 0.15
    else:
        im = pag * 0.10

total = pag + im

print("El pago es de: ", pag)
print("El impuesto es de: ", im)
print("para un total de: ", total)
