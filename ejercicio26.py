def convertir_horas_a_segundos(horas):
    segundos = horas * 3600
    return segundos

# Ejemplo de uso
horas = float(input("Ingrese la cantidad de horas: "))

segundos = convertir_horas_a_segundos(horas)
print(f"{horas} horas equivalen a {segundos} segundos")