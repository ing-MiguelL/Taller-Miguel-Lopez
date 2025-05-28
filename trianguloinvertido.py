def imprimir_triangulo_invertido(n):
    for i in range(n, 0, -1):  
        print("*" * i)

altura = int(input("Ingrese la altura del triángulo: "))
imprimir_triangulo_invertido(altura)

input("Presiona Enter para salir...")