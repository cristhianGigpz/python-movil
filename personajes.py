def agregar_despedida(clss):
    def despedirse(self, mensaje):
        return f"Adiós, soy {self.nombre}, {mensaje}"
    
    clss.despedirse = despedirse
    return clss

@agregar_despedida
class Personaje:
    def __init__(self, nombre, nivel_fuerza, talla, planeta_origen, resistencia=10000):
        self.nombre = nombre
        self.__nivel_fuerza = nivel_fuerza
        self.talla = talla
        self.planeta_origen = planeta_origen
        self.resistencia = resistencia
    
    def saludar(self):
        return f"Hola, soy {self.nombre}"
    
    @property
    def nivel_fuerza(self):
        return self.__nivel_fuerza
    
    @nivel_fuerza.setter
    def nivel_fuerza(self, nuevo_nivel):
        if nuevo_nivel > 0:
            self.__nivel_fuerza = nuevo_nivel
        else:
            raise ValueError("El nivel de fuerza no puede ser negativo")