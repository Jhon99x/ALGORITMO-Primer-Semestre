'''Pide calificaciones de tareas, proyectos y exámenes y calcula la nota final.'''

tareas = float(input("Ingrese la calificación de tareas (0-100): "))
proyectos = float(input("Ingrese la calificación de proyectos (0-100): "))
examenes = float(input("Ingrese la calificación de exámenes (0-100): "))

notafinal = tareas+proyectos+examenes
print("La nota final es:", notafinal/3)