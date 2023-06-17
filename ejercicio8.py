num = input("Introduzca el numero: ")

num = int(num)

if num >= 0:
    mensaje = f"""el numero es: {num}  positivo"""

elif num < 0:
    mensaje = f"""el numero es: {num} negativo"""

    
print(mensaje)