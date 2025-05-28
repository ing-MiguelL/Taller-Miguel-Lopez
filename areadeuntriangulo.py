def area_triangulo(base, altura):
    return (base * altura) / 2  # Fórmula: (base * altura) / 2

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

print(f"El área del triángulo es: {area_triangulo(base, altura)}")

input("Presiona Enter para salir...")