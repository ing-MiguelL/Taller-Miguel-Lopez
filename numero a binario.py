def decimal_a_binario(n):
    return bin(n)[2:]  # Usamos bin() y eliminamos el prefijo "0b"

numero = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(numero)

print(f"El número {numero} en binario es: {binario}")
input("Presiona Enter para salir...")