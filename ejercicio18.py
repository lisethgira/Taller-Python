
May = 0
Men = 0
MMa = 0
FMe = 0

for c in range(1, 51):
    Ed = int(input("Ingrese la edad: "))
    Sx = input("Ingrese el género (M/F): ")

    if Ed >= 18:
        May += 1
    else:
        Men += 1

    if Sx == "M":
        if Ed >= 18:
            MMa += 1
    else:
        if Ed < 18:
            FMe += 1

PMa = (May * 100) / 50
PMe = (Men * 100) / 50

print("MMa:", MMa)
print("FMe:", FMe)
print("May:", May)
print("Men:", Men)
print("PMa:", PMa)
print("PMe:", PMe)