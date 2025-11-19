'''Pide el número de días de retraso en la devolución de un libro y calcula la multa.'''

multa = 2000
Retraso = int(input("Introduce los dias de retraso: "))
if Retraso > 0:
    Total = multa * Retraso
    print("La multa por", Retraso, "dias de retraso es de $",Total, "pesos.")
else:
    print("No hay multa por devolución a tiempo.")
