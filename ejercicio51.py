exam_fisica = float(input("¿Cual es la calificacion del examen de fisica?: "))
trabajo_f_1 = float(input("¿Cual es la calificacion del trabajo #1 de fisica?: "))
trabajo_f_2= float(input("¿Cual es la calificacion del trabajo #2 de fisica?: "))
exam_quimica = float(input("¿Cual es la calificacion del examen de quimica?: "))
trabajo_q_1 = float(input("¿Cual es la calificacion del trabajo #1 de quimica?: "))
trabajo_q_2 = float(input("¿Cual es la calificacion del trabajo #2 de quimica?: "))
trabajo_q_3 = float(input("¿Cual es la calificacion del trabajo #3 de quimica?: "))
exam_mate = float(input("¿Cual es la calificacion del examen de matematicas?: "))
trabajo_m_1 = float(input("¿Cual es la calificacion del trabajo #1 de matematicas?: "))
trabajo_m_2 = float(input("¿Cual es la calificacion del trabajo #2 de matematicas?: "))
trabajo_m_3 = float(input("¿Cual es la calificacion del trabajo #3 de matematicas?: "))

tarea_f = (trabajo_f_1 + trabajo_f_2)/2
promedio_f = exam_fisica * 0.8 + tarea_f * 0.2

tarea_q = (trabajo_q_1 + trabajo_q_2 + trabajo_q_3)/3
promedio_q = exam_quimica * 0.85 + tarea_q * 0.15

tarea_m = (trabajo_m_1 + trabajo_m_2 + trabajo_m_3)/3
promedio_m = exam_mate * 0.9 + tarea_m * 0.1

promedio = promedio_f + promedio_q + promedio_m

print("el promedio de fisica es: " + str(promedio_f))
print("el promedio de quimica es: " + str(promedio_q))
print("el promedio de matematicas es: " + str(promedio_m))