'''Pide un mes y determina si está dentro del ciclo escolar o en vacaciones.'''

vacaciones = ["abril","julio","octubre","dicembre"]

mes = input("Ingrese un mes:").strip().lower()

if mes in vacaciones:
    print(mes,"se encuentra en vacaciones.")
else:
    print(mes,"se encuentra dentro del ciclo escolar.")