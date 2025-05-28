def eliminar_primero(lista):
    return lista[1:] if lista else lista  # Devuelve la lista sin el primer elemento

numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"Lista sin el primer elemento: {eliminar_primero(numeros)}")

# Esperar a que el usuario presione Enter antes de cerrar
input("Presiona Enter para salir...")