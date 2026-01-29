class Personaje:
    def __init__(self, nombre, nivel_fuerza):
        self.nombre = nombre
        self.__nivel_fuerza = nivel_fuerza

    def saludar(self):
        return f"Hola, soy {self.nombre}"
    
    def get_nivel_fuerza(self):
        return self.__nivel_fuerza
    
    def set_nivel_fuerza(self, nuevo_nivel):
        if nuevo_nivel > 0:
            self.__nivel_fuerza = nuevo_nivel
        else:
            raise ValueError("El nivel de fuerza no puede ser negativo")