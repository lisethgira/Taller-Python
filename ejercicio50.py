primero_i = int(input("Coloque el dinero para la primera inversion: "))
segunda_i = int(input("Coloque el dinero para la segunda inversion: "))
tercera_i = int(input("Coloque el dinero para la tercera inversion: "))

total = primero_i + segunda_i + tercera_i
porcentaje_i = (primero_i * 100)/total
porcentaje_s = (segunda_i * 100)/total
porcentaje_t = (tercera_i * 100)/total

print("La primera persona invirtio el: " + str(porcentaje_i))
print("La segunda persona invirtio el: " + str(porcentaje_s))
print("La tercera persona invirtio el: " + str(porcentaje_t))