import pygame
import constantes

def agregar_despedida(clss):
    def despedirse(self, mensaje):
        return f"Adiós, soy {self.nombre}, {mensaje}"
    
    clss.despedirse = despedirse
    return clss

@agregar_despedida
class Personaje:
    def __init__(self, nombre, nivel_fuerza, talla, planeta_origen, resistencia=20000, x=0, y=0):
        self.nombre = nombre
        self.__nivel_fuerza = nivel_fuerza
        self.talla = talla
        self.planeta_origen = planeta_origen
        self.resistencia = resistencia
        self.x = x
        self.y = y
        self.shape = pygame.Rect(self.x, self.y, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        self.shape.center = (self.x, self.y)
    
    def dibujar(self, screen):
        pygame.draw.rect(screen, "blue", self.shape)
        #pygame.draw.circle(screen, "red", (self.x, self.y), 40)
    
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