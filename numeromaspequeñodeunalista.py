def minimo(lista):
    return min(lista) if lista else None  # Devuelve el menor si la lista no está vacía

numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"El número más pequeño es: {minimo(numeros)}")

# Esperar a que el usuario presione Enter antes de cerrar
input("Presiona Enter para salir...")