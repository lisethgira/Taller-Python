metros = int(input("¿cuantos metros tiene el terreno"))

metros_p = metros * 0.35
metros_c = metros * 0.65

cantidad_p = round(metros_p/10 * 4)
cantidad_c = round(metros_c/15 * 5)

print("la cantidad de pinos a plantar es de: " + str(cantidad_p))
print("la cantidad de cedros a plantar es: " + str(cantidad_c))