def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def encontrar_primos(lista):
    return [num for num in lista if es_primo(num)]

numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"Números primos en la lista: {encontrar_primos(numeros)}")

input("Presiona Enter para salir...")