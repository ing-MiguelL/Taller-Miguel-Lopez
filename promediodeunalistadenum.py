def calcular_promedio(lista):
    return sum(lista) / len(lista) if lista else 0  # Evita división por cero


numeros = list(map(float, input("Ingrese números separados por espacios: ").split()))

promedio = calcular_promedio(numeros)

print(f"El promedio de los números ingresados es: {promedio:.2f}")
input("Presiona Enter para salir...")
