
def calcularBilletesYMonedas(cantidad):
    billetes = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    resultado = {}
    
    for billete in billetes:
        cantidadBilletes = cantidad // billete
        
        if cantidadBilletes > 0:
            resultado[billete] = cantidadBilletes
            cantidad = cantidad % billete
    
    return resultado

cantidadDinero = int(input("Ingrese la cantidad de dinero en pesos: "))
resultado = calcularBilletesYMonedas(cantidadDinero)

print("Para una cantidad de", cantidadDinero, "pesos, se necesitarían:")

for billete, cantidad in resultado.items():
    print(cantidad, "billetes de", billete, "pesos")