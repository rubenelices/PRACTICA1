import matplotlib.pyplot as plt
import numpy as np

class SistemaAsientos:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.asientos = np.zeros((filas, columnas), dtype=int)  # Matriz de asientos (0 = disponible)

    def calcular_prioridad(self, fila, columna, criterio="vista"):
        if criterio == "vista":
            return abs(columna - self.columnas // 2)  # Prioridad en columnas más centradas
        elif criterio == "salida":
            return fila  # Fila 0 es la más cercana a la salida
        else:
            return 0

    def asignar_prioridades(self, criterio="vista"):
        # Genera un diccionario con la prioridad de cada asiento
        prioridades = {}
        for fila in range(self.filas):
            for columna in range(self.columnas):
                prioridad = self.calcular_prioridad(fila, columna, criterio)
                prioridades[(fila, columna)] = prioridad
        return prioridades

    def mostrar_asientos(self, criterio="vista"):
        # Obtener las prioridades de los asientos según el criterio
        prioridades = self.asignar_prioridades(criterio)
        
        # Crear una matriz visual para las prioridades
        matriz_prioridades = np.full((self.filas, self.columnas), np.nan)
        for (fila, columna), prioridad in prioridades.items():
            matriz_prioridades[fila, columna] = prioridad
        
        # Dibujar la cuadrícula de asientos usando matplotlib
        fig, ax = plt.subplots(figsize=(10, 6))
        cax = ax.matshow(matriz_prioridades, cmap="coolwarm", origin="upper")
        fig.colorbar(cax, label="Prioridad (menor es mejor)")
        
        # Añadir etiquetas de los asientos
        for fila in range(self.filas):
            for columna in range(self.columnas):
                prioridad = matriz_prioridades[fila, columna]
                ax.text(columna, fila, f"{int(prioridad)}", va='center', ha='center', color="black")
        
        # Configuración del gráfico
        ax.set_title(f"Asientos ordenados por: {criterio.capitalize()}")
        ax.set_xlabel("Columna")
        ax.set_ylabel("Fila")
        ax.set_xticks(range(self.columnas))
        ax.set_yticks(range(self.filas))
        ax.invert_yaxis()  # Para que la fila 0 esté arriba, como en un avión

        plt.show()

# Uso del sistema de asientos
if __name__ == "__main__":
    filas = 10
    columnas = 6
    sistema = SistemaAsientos(filas, columnas)

    # Solicitar al usuario el criterio de prioridad
    criterio = input("Seleccione el criterio para ordenar los asientos ('vista' o 'salida'): ").strip().lower()
    if criterio not in {"vista", "salida"}:
        print("Criterio no válido. Usando 'vista' por defecto.")
        criterio = "vista"

    sistema.mostrar_asientos(criterio)
