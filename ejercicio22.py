
def calcular_puntuacion_z(dato, media, desviacion_estandar):
    z = (dato - media) / desviacion_estandar
    return z

# Ejemplo de uso
dato = float(input("Ingrese el dato: "))
media = float(input("Ingrese la media: "))
desviacion_estandar = float(input("Ingrese la desviación estándar: "))

puntuacion_z = calcular_puntuacion_z(dato, media, desviacion_estandar)
print("La puntuación Z del dato es:", puntuacion_z)