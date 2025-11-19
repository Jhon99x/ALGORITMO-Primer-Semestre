'''Pide peso y altura, calcula el IMC y clasifícalo en "Bajo peso", "Normal", "Sobrepeso" o
"Obesidad".'''
peso = float(input("Ingrese su peso en kg:"))
altura = float(input("Ingrese su altura en mts:"))

alturapow = pow(altura,2)
imc = peso/alturapow

if imc <18:
    print("Bajo peso.")
elif 18<= imc <=24:
    print("Peso normal.")
elif 25<= imc <=39:
    print("Sobrepeso.")
elif imc >40:
    print("Obesidad.")
