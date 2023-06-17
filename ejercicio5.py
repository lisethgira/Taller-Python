import math

while True: 
    try:
        Valor1 = float(input("Ingrese el primer valor: "))
        Valor2 = float(input("Ingrese el segundo valor: "))
        Valor3 = float(input("Ingrese el tercer valor: "))
        
        if Valor1 <= 0 or Valor2 <= 0 or Valor3 <= 0:
            print("Los valores deben ser positivos. Intente de nuevo.")
            continue
        break
    
    except ValueError:
        print("Porfavor ingrese un numero valido")
        
Volumen = Valor1 * Valor2 * Valor3 
    
print("El volumen es: ", Volumen)