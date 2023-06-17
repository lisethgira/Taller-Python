nota = int(input("nota"))

promedio = 0
acumula = 0
cuenta = 0

while nota != 0:
    cuenta = cuenta + 1
    acumula = acumula + nota
    nota = nota - 1

promedio = float(acumula) / float(cuenta) 

print ("promedio:", promedio)