sw = 0
s = 0

while sw == 0:
    ficha = {
        "nombre": "",
        "categoria": "",
        "edad": 0,
        "sueldo": 0
    }

    ficha["nombre"] = input("Ingrese el nombre: ")
    ficha["categoria"] = input("Ingrese la categoría: ")
    ficha["edad"] = int(input("Ingrese la edad: "))
    ficha["sueldo"] = float(input("Ingrese el sueldo: "))

    print(ficha)

    if ficha["edad"] > 65:
        s += 1
        sw = 1

if sw == 1:
    print("Existen trabajadores...")
    print(s)




