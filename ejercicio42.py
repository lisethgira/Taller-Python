nombre = input("Nombre del estudiante: ")
nota_s = float(input("Nota de seguimiento: "))
nota_p = float(input("Nota parcial: "))
nota_py = float(input("Nota proyecto: "))
nota_f = float(input("Nota final: "))



nota_s = nota_s * 0.4
nota_p = nota_p * 0.2
nota_py = nota_py * 0.1
nota_f = nota_f * 0.3

porcentaje_final = nota_s + nota_p + nota_py + nota_f

mensaje = "El estudiante " + str(nombre) + "tuvo como promedio: " + str(porcentaje_final)

print(mensaje)