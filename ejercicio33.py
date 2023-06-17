while True:
    try:
        Centimetro = float(input("Porfavor ingrese los centimetros a convertir"))
        if Centimetro <= 0:
            print("Porfavor ingrese valores positivos: ")
            continue
        break
    
    except ValueError:
        print ("Porfavor ingresa un numero valido: ")
                
Pulgadas = Centimetro /2.54

print("Laas pulgadas son: ", Pulgadas)