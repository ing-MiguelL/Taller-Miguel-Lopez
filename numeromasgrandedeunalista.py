def maximo(lista):
    return max(lista) if lista else None  # Devuelve el mayor si la lista no está vacía

numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"El número más grande es: {maximo(numeros)}")

# Esperar a que el usuario presione Enter antes de cerrar
input("Presiona Enter para salir...")