def calcular_calorias(peso, altura, edad, sexo, actividad):
    if sexo.lower() == "hombre":
        metabolismo_basal = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * edad)
    else:
        metabolismo_basal = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * edad)

    factores_actividad = {
        "sedentario": 1.2,
        "ligero": 1.375,
        "moderado": 1.55,
        "activo": 1.725,
        "muy activo": 1.9
    }

    return metabolismo_basal * factores_actividad.get(actividad.lower(), 1.2)

# Solicitar datos al usuario
peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (cm): "))
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (hombre/mujer): ")
actividad = input("Ingrese su nivel de actividad (sedentario, ligero, moderado, activo, muy activo): ")

calorias_diarias = calcular_calorias(peso, altura, edad, sexo, actividad)

print(f"Su consumo diario recomendado es: {calorias_diarias:.2f} kcal.")

input("Presiona Enter para salir...")