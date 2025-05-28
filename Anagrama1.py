def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())  

texto1 = input("Ingrese la primera palabra: ")
texto2 = input("Ingrese la segunda palabra: ")

print(f'"{texto1}" y "{texto2}" {"son anagramas" if son_anagramas(texto1, texto2) else "no son anagramas"}.')
input("presione enter")