'''Pide un día de la semana y determina si es fin de semana o día laboral.'''

finSemana = ["sábado", "domingo"]
semana = ["lunes", "martes", "miércoles", "jueves", "viernes"]

dia = input("Ingrese un día de la semana: ").lower()

if dia in finSemana:
    print(dia, "es fin de semana.")
elif dia in semana:
    print(dia, "es un día laboral.")
