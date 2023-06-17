

def convertir_minutos_a_horas(minutos):
    horas = minutos // 60  # Dividir entre 60 para obtener las horas completas
    minutos_restantes = minutos % 60  # Calcular los minutos restantes
    return horas, minutos_restantes

# Ejemplo de uso
minutos_totales = int(input("Ingrese la cantidad de minutos: "))
horas, minutos = convertir_minutos_a_horas(minutos_totales)
print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos.")