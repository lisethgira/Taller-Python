def calcular_anualidades(prestamo, tiempo, interes):
    anualidad = (prestamo / tiempo) * interes
    return anualidad

# Ejemplo de uso
prestamo = float(input("Ingrese el monto del préstamo: "))
tiempo = int(input("Ingrese el tiempo en años: "))
interes = float(input("Ingrese la tasa de interés anual: "))

anualidad = calcular_anualidades(prestamo, tiempo, interes)
print("La anualidad a pagar es:", anualidad)