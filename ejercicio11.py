compra = input("Ingrese la compra: ")
valor = input("Ingrese el valor de la compra: ")
cliente = input("tipo de cliente: ")

valor = int(valor)

if cliente == "a":
    precio = valor - (valor * 0.1)
else:
    if cliente == "b":
        precio = valor - (valor * 0.15)
    else:
        if cliente == "c": 
            precio = valor - (valor * 0.2)

print(precio)