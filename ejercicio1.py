#Funcion para calcular el Volumen y Area de un cilindro con los datos de Radio y Altura
import math

def AreayVolumenCilindro(Radio, Altura):
    Area = 2 * math.pi * Radio * (Radio + Altura)
    Volumen = math.pi * Radio**2 * Altura
    
    return [Area, Volumen]
    

Radio=float(input("Porfavor ingrese el radio del cilindro: "))
Altura=float(input("Porfavor ingrese la altura del cilindro: "))

[Area,Volumen] = AreayVolumenCilindro(Radio, Altura)

print ("El area del cilindro es: ", Area, " El Volumen del cilindro es: ", Volumen)
