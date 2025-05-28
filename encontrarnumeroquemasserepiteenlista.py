from collections import Counter

def numero_mas_repetido(lista):
    contador = Counter(lista)
    return max(contador, key=contador.get)  # Encuentra el número con mayor frecuencia

numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"El número más repetido es: {numero_mas_repetido(numeros)}")
input("Presiona Enter para salir...")