'''Pide un tipo de sangre y determina a qué grupos puede donar y recibir.'''

tipo_sangre = input("Ingrese su tipo de sangre (A, B, AB, O): ").strip().upper()

if tipo_sangre == "A":
    print("Puede donar a: A, AB")
    print("Puede recibir de: A, AB")
elif tipo_sangre == "B":
    print("Puede donar a: B, AB")
    print("Puede recibir de: B, AB")
elif tipo_sangre == "AB":
    print("Puede donar a: AB")
    print("Puede recibir de: A, B, AB")
elif tipo_sangre == "O":
    print("Puede donar a: O")
    print("Puede recibir de: O")