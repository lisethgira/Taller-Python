precio_tarifa = float(input("Ingrese el precio de la tarifa: "))
precio_pagado = float(input("Ingrese el precio pagado: "))

diferencia = precio_tarifa - precio_pagado
porcentaje_descontado = (diferencia / precio_tarifa) * 100

print("El porcentaje descontado es:", porcentaje_descontado, "%")