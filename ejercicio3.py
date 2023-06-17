while True:
    try:
        Valor1 = float(input("Ingrese el primer valor"))
        Valor2 = float(input("Ingrese el segundo valor"))
        Valor3 = float(input("Ingrese el tercer valor")) 
          
        if Valor1==Valor2 or Valor1==Valor3 or Valor2==Valor3:
              print("Por favor, no ingrese números iguales.")
              
        else:
            break
        
    except ValueError:
        print("Por favor, ingrese un valor válido.")
        
mayor = Valor1
menor = Valor1

if Valor2 > mayor:
    mayor = Valor2
    
if Valor3 > mayor:
    mayor = Valor3
    
if Valor2 < menor:
    menor = Valor2
    
if Valor3 < menor:
    menor = Valor3
     
print("El valor mayor es:", mayor, " El valor menor es:", menor)