def contar_digitos(n):
    return len(str(abs(n)))  # Convertimos el número a positivo y contamos los caracteres

numero = int(input("Ingrese un número entero: "))
cantidad_digitos = contar_digitos(numero)

print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
input("Presiona Enter para salir...")