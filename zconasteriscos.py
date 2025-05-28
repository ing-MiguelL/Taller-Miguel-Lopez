def imprimir_z(n):
    for i in range(n):
        if i == 0 or i == n - 1:  
            print("*" * n)
        else: 
            print(" " * (n - i - 1) + "*")

tamaño = int(input("Ingrese el tamaño de la 'Z': "))
imprimir_z(tamaño)


input("Presiona Enter para salir...")