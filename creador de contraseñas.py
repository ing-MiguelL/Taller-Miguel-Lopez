import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation 
    return "".join(random.choice(caracteres) for _ in range(longitud))

longitud = int(input("Ingrese la longitud de la contraseña: "))
print(f"Contraseña generada: {generar_contrasena(longitud)}")

input("Presiona Enter para salir...")