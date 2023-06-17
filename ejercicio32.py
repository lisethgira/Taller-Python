def AreayPerimetrodeunTriangulo(Base, Altura, L2, L3):
    Area = (Base * Altura) / 2
    Perimetro = Base + L2 + L3
    
    return [Area, Perimetro]
    
while True:
    try:
        Base = float(input("Porfavor ingrese la base del triangulo: "))
        if Base <= 0:
            print("Porfavor ingrese un valor numerico positivo: ")
            continue
        
        Altura = float(input("Porfavor ingrese el altura del triangulo: "))
        if Altura <= 0:
            print("Porfavor ingrese un valor numerico positivo: ")
            continue
        
        L2 = float(input("Porfavor ingrese uno de sus lados del triangulo: "))
        if L2 <= 0:
            print("Porfavor ingrese un valor numerico positivo: ")
            continue
        
        L3 = float(input("Porfavor ingrese la vase del triangulo: "))
        if L3 <= 0:
            print("Porfavor ingrese un valor numerico positivo: ")
            continue
        
        break
    except ValueError:
        print("Porfavor ingrgese un valor numerico valido: ")
            
            
[Area, Perimetro] = AreayPerimetrodeunTriangulo (Base, Altura, L2, L3)
    
print ("El area del triangulo es: ", Area)
print ("El perimetro del triangulo es: ", Perimetro)
    