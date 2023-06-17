codigo_producto_a = input("Codigo de producto: ")
sub_total = 0

while codigo_producto_a != "":
    precio = int(input("Precio: "))
    sub_total = sub_total + precio
    codigo_producto_a = input("Codigo de producto: ")


iva = sub_total * 0.15
total = sub_total + iva

print("Sub total: ", sub_total)
print("Iva: ", iva)
print("Total: ", total)