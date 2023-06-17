def calcular_fuerza(trabajo, tiempo):
    fuerza = trabajo / tiempo
    return fuerza

# Ejemplo de uso
trabajo = float(input("Ingrese el valor del trabajo realizado: "))
tiempo = float(input("Ingrese el tiempo transcurrido: "))

fuerza = calcular_fuerza(trabajo, tiempo)
print("La fuerza es:", fuerza)