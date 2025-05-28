def contar_apariciones(lista, numero):
    return lista.count(numero)  # lo usamos count() para contar ocurrencias

numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
num_buscar = int(input("Ingrese el número que desea contar: "))

print(f"El número {num_buscar} aparece {contar_apariciones(numeros, num_buscar)} veces.")
input("Presiona Enter para salir...")