def invertir_lista(lista):
    lista_invertida = []
    for i in range(len(lista)):  # Iteramos desde el último hasta el primero
        lista_invertida.append(lista[len(lista) - 1 - i])
    return lista_invertida

numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"Lista invertida: {invertir_lista(numeros)}")
input("Presiona Enter para salir...")