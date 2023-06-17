
def calcular_total_boletos(num_boletos, precio_boletos):
    total_pagar = num_boletos * precio_boletos
    return total_pagar

# Ejemplo de uso
num_boletos = int(input("Ingrese el número de boletos a comprar: "))
precio_boletos = float(input("Ingrese el precio del boleto: "))
  
total_pagar = calcular_total_boletos(num_boletos, precio_boletos)
print("El total a pagar es:", total_pagar)