Personas = int(input('Número de personas: '))

print('Kilo de arroz = 50 euros')
print('Kilo de camarones = 100 euros')

IngredienteArroz = ((500 * Personas) / 4) / 1000
print(str(IngredienteArroz) + ' kg' + ' de arroz')

IngredienteCamaron = (Personas * 0.25) / 4
print(str(IngredienteCamaron) + ' kg' + ' de camarón')

Coste = (IngredienteArroz * 50) + (IngredienteCamaron * 100)
print(str(Coste) + ' euros')