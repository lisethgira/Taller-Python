def SueldoPorHoras (HorasTrabajadas):
    SueldoSemanal = HorasTrabajadas * 4.833 
    
    return [SueldoSemanal]


while True: 
    try:
        HorasTrabajadas = float(input("Porfavor ingrese las horas trabajadas a la semana: "))
        
        if HorasTrabajadas <= 0:
            print("Porfavor ingrese valores positivos:")
            continue
        break
    
    except ValueError:
        print("Porfavor ingrese un valor numerico valido: ")
        
[SueldoSemanal] = SueldoPorHoras(HorasTrabajadas)

print("El valor a pagar es: ", SueldoSemanal)
                                                           