import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)  
    intentos = 0

    print(" ¡Bienvenido al juego de adivinanza!")
    print("Adivina el número secreto entre 1 y 100.")

    while True:
        try:
            intento = int(input("Ingrese su número: "))
            intentos += 1

            if intento < numero_secreto:
                print(" Demasiado bajo. Intenta de nuevo.")
            elif intento > numero_secreto:
                print(" Demasiado alto. Intenta de nuevo.")
            else:
                print(f" ¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Error: Ingresa un número válido.")

    input("Presiona Enter para salir...")

juego_adivinanza()