

NP = 0
NI = 0
Num = None

while True:
    Num = int(input("Ingrese un número: "))

    if Num != 0:
        if Num % 2 == 0:
            NP += 1
        else:
            NI += 1
    else:
        break

print("Numeros pares:", NP)
print("Numeros impares:", NI)