

tarifa = float(input("Ingrese la tarifa: "))
N = int(input("Ingrese el valor de N: "))
C = 1
i = 0

while C <= N:
    horas = float(input("Ingrese las horas trabajadas: "))
    salario = tarifa * horas
    
    if salario >= 500:
        i += 1
    
    C += 1

print(i)