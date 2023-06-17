hombres = int(input("Cuantos hombres hay en el grupo: "))
mujeres = int(input("Cuantas mujeres hay en el grupo: "))

grupo = hombres + mujeres

porcentaje_h = hombres * 100/grupo
porcentaje_m = mujeres * 100/grupo

print("el porcentaje de hombres es: " + str(porcentaje_h)) 
print("el porcentaje de mujeres es : " + str(porcentaje_m))