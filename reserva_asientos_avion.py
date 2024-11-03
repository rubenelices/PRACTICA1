class Asientos:
    def __init__(self, filas, columnas):
        self.asientos = [[False for _ in range(columnas)] for _ in range(filas)]
        self.filas = filas
        self.columnas = columnas


    def mostrar_asientos(self):
        for fila in self.asientos:
            print(" ".join(["X" if asiento else "0" for asiento in fila]))


    def reservar_asiento(self, fila, columna):
        if not self.asientos[fila][columna]:
            self.asientos[fila][columna] = True
            print(f"Asiento en fila {fila + 1}, columna {columna + 1} reservado.")
            return True
        else:
            print("El asiento ya está ocupado.")
            return False


    def cancelar_reserva(self, fila, columna):
        if self.asientos[fila][columna]:
            self.asientos[fila][columna] = False
            print(f"Reserva en fila {fila + 1}, columna {columna + 1} cancelada.")
            return True
        else:
            print("El asiento ya estaba libre.")
            return False


    def buscar_asientos_contiguos(self, cantidad):
        for i, fila in enumerate(self.asientos):
            contiguos = 0
            for j in range(self.columnas):
                if not fila[j]:
                    contiguos += 1
                    if contiguos == cantidad:
                        return [(i, col) for col in range(j - cantidad + 1, j + 1)]
                else:
                    contiguos = 0
        print("No se encontraron suficientes asientos contiguos.")
        return []


    def buscar_asientos_ventana(self):
        # Encuentra los asientos en los extremos de cada fila (ventanas)
        asientos_ventana = []
        for i in range(self.filas):
            # Primer asiento de la fila (columna 0)
            if not self.asientos[i][0]:
                asientos_ventana.append((i, 0))
            # Último asiento de la fila (columna -1)
            if not self.asientos[i][self.columnas - 1]:
                asientos_ventana.append((i, self.columnas - 1))
        return asientos_ventana



class SistemaReservas:
    def __init__(self, filas, columnas):
        self.asientos = Asientos(filas, columnas)


    def mostrar_asientos_disponibles(self):
        print("Estado actual de los asientos (0 = Libre, X = Ocupado):")
        self.asientos.mostrar_asientos()


    def reservar(self, fila, columna):
        return self.asientos.reservar_asiento(fila - 1, columna - 1)


    def cancelar(self, fila, columna):
        return self.asientos.cancelar_reserva(fila - 1, columna - 1)


    def buscar_asientos_optimos(self, cantidad):
        # Devuelve los asientos contiguos directamente
        return self.asientos.buscar_asientos_contiguos(cantidad)


    def reservar_asientos_contiguos(self, asientos):
        # Pregunta al usuario si desea reservar los asientos contiguos encontrados
        reserva_contiguos = input("¿Desea reservar estos asientos? (si/no): ").lower()
        if reserva_contiguos == "si":
            for fila, columna in asientos:  
                self.asientos.reservar_asiento(fila, columna)
            print("Reservados los asientos:", [(f + 1, c + 1) for f, c in asientos])
        else:
            print("No se reservarán los asientos contiguos.")


    def reservar_asientos_ventana(self):
        # Buscar asientos en las ventanas (extremos)
        asientos_ventana = self.asientos.buscar_asientos_ventana()
        if asientos_ventana:
            print("Asientos de ventana disponibles:", [(f + 1, c + 1) for f, c in asientos_ventana])
            for fila, columna in asientos_ventana:
                # Preguntar si el usuario quiere reservar cada asiento de ventana disponible
                respuesta = input(f"¿Desea reservar el asiento de ventana en fila {fila + 1}, columna {columna + 1}? (s/n): ").lower()
                if respuesta == "s":
                    self.asientos.reservar_asiento(fila, columna)
                    break
        else:
            print("No hay asientos de ventana disponibles.")
        


def menu():
    print("\n--- Menú del Sistema de Reservas ---")
    print("1. Ver asientos disponibles")
    print("2. Reservar asiento")
    print("3. Cancelar reserva")
    print("4. Buscar y reservar asientos contiguos")
    print("5. Buscar y reservar asientos con ventana")
    print("6. Salir")


def main():
    filas = 10
    columnas = 6
    sistema = SistemaReservas(filas, columnas)


    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.mostrar_asientos_disponibles()

        elif opcion == "2":
            fila = int(input("Ingrese el número de fila: "))
            columna = int(input("Ingrese el número de columna: "))
            sistema.reservar(fila, columna)

        elif opcion == "3":
            fila = int(input("Ingrese el número de fila: "))
            columna = int(input("Ingrese el número de columna: "))
            sistema.cancelar(fila, columna)

        elif opcion == "4":
            cantidad = int(input("¿Cuántos asientos contiguos necesita? "))
            asientos = sistema.buscar_asientos_optimos(cantidad)
            if asientos:
                print("Asientos contiguos encontrados:", [(f + 1, c + 1) for f, c in asientos])
                # Llamamos a la función para preguntar si desea reservar los asientos
                sistema.reservar_asientos_contiguos(asientos)
            else:
                print("No se encontraron suficientes asientos contiguos.")

        elif opcion == "5":
            sistema.reservar_asientos_ventana()

        elif opcion == "6":
            print("Saliendo del sistema de reservas.")
            break

        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    main()
