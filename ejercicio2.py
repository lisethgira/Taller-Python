while True: 
    try:
        Valor1 = float(input("Ingrese el primer valor: "))
        Valor2 = float(input("Ingrese el segundo valor: "))
        break
    except ValueError:
        print("Porfavor ingrese un numero valido")
        
if Valor1 > Valor2:
    mayor = Valor1
else: 
    mayor = Valor2
    
print("El numero mayor es:", mayor)