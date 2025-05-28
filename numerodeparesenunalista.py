def contar_pares(lista):
    return sum(1 for num in lista if num % 2 == 0)  # Cuenta los números divisibles por 2

numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"Cantidad de números pares en la lista: {contar_pares(numeros)}")

# Esperar a que el usuario presione Enter antes de cerrar
input("Presiona Enter para salir...")