'''Pide una temperatura y clasifícala como "Muy frío", "Frío", "Tibio", "Caliente", o "Muy
caliente".'''

temperatura = float(input("Ingrese una temperatura:"))

if 0<= temperatura <=19:
    print("Muy frio")
elif 20<= temperatura <= 30:
    print("Frio")
elif 31<= temperatura <= 40:
    print("Tibio")
elif 41<= temperatura <= 50:
    print("Caliente")
else:
    print("Muy caliente")