def rotar_lista(lista):
    return [lista[-1]] + lista[:-1] if lista else lista  

numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"Lista rotada: {rotar_lista(numeros)}")
input("Presiona Enter para salir...")