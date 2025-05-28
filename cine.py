class Cine:
    def __init__(self, nombre, filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.asientos = [["O" for _ in range(columnas)] for _ in range(filas)]  # 'O' significa un asiento disponible

    def mostrar_asientos(self):
        print(f"\nMapa de asientos en {self.nombre}:")
        print("   " + " ".join(str(j) for j in range(self.columnas)))  # aca vemos el Índices de columnas
        for i, fila in enumerate(self.asientos):
            print(f"{i} {' '.join(fila)}")  # nos muestra el índice de cada fila

    def reservar_asiento(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:  # Verifica límites
            if self.asientos[fila][columna] == "O":
                self.asientos[fila][columna] = "X"  # Marca como reservado
                print("\n Reserva exitosa")
            else:
                print("\n El asiento ya está ocupado. Intente otro.")
        else:
            print("\n Fila o columna no válidas. Intente de nuevo.")

# Configuración del cine
cine = Cine("Cine Estelar", 5, 5)

while True:
    cine.mostrar_asientos()
    try:
        fila = int(input("\nIngrese la fila para reservar (0-4): "))
        columna = int(input("Ingrese la columna para reservar (0-4): "))
        cine.reservar_asiento(fila, columna)
    except ValueError:
        print("\n Error: Ingrese números válidos.")

    continuar = input("\n¿Desea reservar otro asiento? (s/n): ").lower()
    if continuar != "s":
        break

print("\n Gracias por usar el sistema de reservas.")
input("presiona enter para cerrar el progtama de cine")