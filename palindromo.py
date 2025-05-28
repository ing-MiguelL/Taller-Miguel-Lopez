def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")  # Convertimos a minúsculas y eliminamos espacios
    return palabra == palabra[::-1]  # Comparamos la palabra con su versión invertida

texto = input("Ingrese una palabra o frase: ")
resultado = "es un palíndromo" if es_palindromo(texto) else "no es un palíndromo"

print(f'"{texto}" {resultado}.')
input("Presiona Enter para salir...")