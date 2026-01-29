class Personaje:
    def __init__(self, nombre, nivel_fuerza):
        self.nombre = nombre
        self.nivel_fuerza = nivel_fuerza

    def saludar(self):
        return f"Hola, soy {self.nombre} y estoy en el nivel {self.nivel_fuerza}."