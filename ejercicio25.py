def calcular_ganancias(horas_trabajadas, pago_por_hora):
    ganancias = horas_trabajadas * pago_por_hora
    return ganancias

# Ejemplo de uso
horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
pago_por_hora = float(input("Ingrese el pago por hora: "))

ganancias = calcular_ganancias(horas_trabajadas, pago_por_hora)
print("Las ganancias totales son:", ganancias)