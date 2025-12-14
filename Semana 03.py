# ============================================
# Programación Orientada a Objetos (POO)
# Promedio semanal del clima
# ============================================

class Clima:
    def _init_(self):
        # Encapsulamiento: atributo privado
        self.__temperaturas = []

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        return sum(self._temperaturas) / len(self._temperaturas)

# Programa principal
def main():
    print("Promedio semanal del clima - Programación Orientada a Objetos")
    clima = Clima()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")

main()