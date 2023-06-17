numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Operaciones aritméticas básicas
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
resto = numero1 % numero2

# Mostrar resultados de las operaciones
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Resto:", resto)

# Comprobar si las operaciones son conmutativas
if suma != numero2 + numero1:
    suma_conmutativa = numero2 + numero1
    print("Suma conmutativa:", suma_conmutativa)

if resta != numero2 - numero1:
    resta_conmutativa = numero2 - numero1
    print("Resta conmutativa:", resta_conmutativa)

if multiplicacion != numero2 * numero1:
    multiplicacion_conmutativa = numero2 * numero1
    print("Multiplicación conmutativa:", multiplicacion_conmutativa)

if division != numero2 / numero1:
    division_conmutativa = numero2 / numero1
    print("División conmutativa:", division_conmutativa)

if resto != numero2 % numero1:
    resto_conmutativa = numero2 % numero1
    print("Resto conmutativa:", resto_conmutativa)