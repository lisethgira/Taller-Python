import math

def PagoPorGalondeLeche (Litro):
    Galones = Litro / 3.785
    
    return [Galones]

Litro = float(input("Porfavor ingrese los litros producidos hoy: "))
ValorG = float(input("Ingrese el valor a pagar por cada galon: "))

[Galones] = PagoPorGalondeLeche (Litro)

Pago = Galones * ValorG

print("Los galones producidos son:", Galones)
print("El valor a pagar por el producido es: ", Pago)