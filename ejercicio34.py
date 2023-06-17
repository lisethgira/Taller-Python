import math
def ConvertirTiempo(Segundos):
    Horas = math.floor(Segundos / 3600)
    Minutos = math.floor((Segundos % 3600) / 60)
    Segundos = Segundos % 60
    
    return [Horas, Minutos, Segundos]
    
while True:
    try:
        Segundos = float(input("Porfavor ingrese los segundos a convertir"))
        if Segundos <= 0:
            print("Porfavor ingrese valores positivos: ")
            continue
        break
    
    except ValueError:
        print ("Porfavor ingresa un numero valido: ")

[Horas, Minutos, Segundos] = ConvertirTiempo (Segundos)

print("las horas son: ", Horas, "Los minutos: ", Minutos, "Los segundos: ", Segundos)