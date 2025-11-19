'''Pide una temperatura en grados Celsius y convierte a Fahrenheit o Kelvin.'''

temperatura = float(input("Ingrese la temperatura en Celsius:"))
fahrenheit = (temperatura * 9/5) + 32
kelvin = temperatura + 273.15
print("La temperatura en Fahrenheit es:",fahrenheit)
print("La temperatura en Kelvin es:",kelvin)