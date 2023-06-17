primer_valor = input("Introduzca el primer valor:")
segundo_valor = input("Introduzca el segundo valor:")
tercer_valor = input("Introduzca el tercer valor:")

primer_valor = int(primer_valor)
segundo_valor = int(segundo_valor)
tercer_valor = int(tercer_valor)

if primer_valor > segundo_valor:
    if primer_valor > tercer_valor:
        mayor = primer_valor

    else: mayor = tercer_valor

else:
    if segundo_valor > tercer_valor:
        mayor = segundo_valor
    else: mayor = tercer_valor

print("el numero" , mayor, "es el mayor")



