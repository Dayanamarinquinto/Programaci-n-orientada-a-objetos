# ============================================
#     Clase base: Vehiculo
# ============================================

# --------------------------------------------
# 1. ABSTRACCIÓN (aplicada en la clase Vehiculo)
# --------------------------------------------
# La abstracción permite representar lo esencial
# de un vehículo sin detalles innecesarios.
# Solo contiene atributos básicos:
# marca, modelo, año y velocidad.
# --------------------------------------------

class Vehiculo:
    def _init_(self, marca, modelo, año, velocidad):
        # =====================================================
        # 2. ENCAPSULAMIENTO (protección de los datos)
        # -----------------------------------------------------
        # Se utilizan atributos con guion bajo y métodos
        # getters y setters para controlar el acceso
        # a los atributos.
        # =====================================================
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._velocidad = velocidad

    # --------- MÉTODO DE ABSTRACCIÓN ------------
    def mostrar_info(self):
        return (f"{self._marca} {self._modelo} "
                f"({self._año}) - Velocidad: {self._velocidad} km/h")

    # --------- MÉTODOS DE ENCAPSULAMIENTO ---------
    def get_velocidad(self):
        return self._velocidad

    def set_velocidad(self, nueva_velocidad):
        if nueva_velocidad >= 0:
            self._velocidad = nueva_velocidad


# ============================================
#        HERENCIA: Auto y Moto
# ============================================

# ---------------------------------------------------------
# 3. HERENCIA
# Auto y Moto heredan de Vehiculo, reutilizando sus atributos.
# ---------------------------------------------------------

class Auto(Vehiculo):
    def _init_(self, marca, modelo, año, velocidad, puertas):
        super()._init_(marca, modelo, año, velocidad)
        self.puertas = puertas

    #