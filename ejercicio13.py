obreros = 50 
total_nomina = 0

for i in range(obreros):
    horas = int(input("Ingrese horas trabajadas: "))
    salario = horas * 30000
    total_nomina = total_nomina + salario

print("Total: ", total_nomina)