def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)  # Fórmula IMC = peso / altura²
    return imc

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
categoria = clasificar_imc(imc)

print(f"\n Su IMC es: {imc:.2f}")
print(f" Clasificación: {categoria}")

input("\nPresiona Enter para salir...")