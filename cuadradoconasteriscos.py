def imprimir_cuadrado(n):
    for _ in range(n):
        print("* " * n)  

lado = int(input("Ingrese el tamaño del cuadrado: "))
imprimir_cuadrado(lado)

input("Presiona Enter para salir...")