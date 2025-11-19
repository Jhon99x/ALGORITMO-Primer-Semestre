'''Pide un usuario y contraseña y verifica si coinciden con valores predeterminados.'''

usuario_correcto = "jhon"
contrasena_correcta = "1234"

usuario = input("Ingresa tu usuario: ")
contrasena = input("Ingresa tu contraseña: ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Acceso concedido")
else:
    print("Usuario o contraseña incorrectos")
