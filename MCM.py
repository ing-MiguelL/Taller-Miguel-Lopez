import math

def mcm(a, b):
    return abs(a * b) // math.gcd(a, b)  

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print(f"El MCM de {num1} y {num2} es: {mcm(num1, num2)}")
input("Presiona Enter para salir...")