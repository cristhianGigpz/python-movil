from personajes import Personaje

class Saiyajin(Personaje):
    def __init__(self, nombre, nivel_fuerza, talla, planeta_origen, cola = True):
        super().__init__(nombre, nivel_fuerza, talla, planeta_origen)
        self.cola = cola

    def transformarse_en_super_saiyajin(self):
        nuevo_nivel = self.get_nivel_fuerza() * 100
        self.set_nivel_fuerza(nuevo_nivel)
        return f"{self.nombre} se ha transformado en Super Saiyajin! Nivel de fuerza: {self.get_nivel_fuerza()}"

    def saludar(self):
        return f"Hola, soy {self.nombre} y soy un Saiyajin"