def CostoGasolina ():
    GasolinaCienKilometros = (100 * Gasolina) / Kilometros
    PrecioGasolina = (100 * Precio) / Kilometros
    GasolinaenunKilometro = Gasolina / Kilometros
    PrecioPorKilometro = Precio / Kilometros
    VelocidadMedia = (Kilometros * Horas) / 2;
    VelocidadMS = VelocidadMedia * 1000;
    
    return[GasolinaCienKilometros, PrecioGasolina, GasolinaenunKilometro, PrecioPorKilometro, VelocidadMedia, VelocidadMS]

while True:
    try:
        Kilometros = float(input("Porfavor ingrese los kilometros recorridos: "))
        if Kilometros <= 0:
            print("Por favor ingrese un valor numerico positivo: ")
            continue
        Gasolina = float(input("Porfavor ingrese la cantidad de gasolina consumida: "))
        if Gasolina <= 0:
            print("Por favor ingrese un valor numerico positivo: ")
            continue
        Precio = float(input("Porfavor ingrese el precio de la gasolina: "))
        if Precio <= 0:
            print("Por favor ingrese un valor numerico positivo: ")
            continue
        Horas = float(input("Porfavor ingrese las horas de viaje: "))
        if Horas <= 0:
            print("Por favor ingrese un valor numerico positivo: ")
            continue
        break
        
    except ValueError:
        print("Por favor ingrese un valor numerico valido.")

[GasolinaCienKilometros, PrecioGasolina, GasolinaenunKilometro, PrecioPorKilometro, VelocidadMedia, VelocidadMS] = CostoGasolina ()
    
print ("Consumo de gasolina en 100 kilometros: ", GasolinaCienKilometros, "Precio en un kilometro: ", PrecioPorKilometro, "Velocidad media km/h: ", VelocidadMedia, "Velocidad media m/s: ", VelocidadMS)


