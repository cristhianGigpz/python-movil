import pygame
#import time

def agregar_despedida(clss):
    def despedirse(self, mensaje):
        return f"Adiós, soy {self.nombre}, {mensaje}"
    
    clss.despedirse = despedirse
    return clss

@agregar_despedida
class Personaje:
    def __init__(self, nombre, nivel_fuerza, talla, planeta_origen, resistencia=20000, x=0, y=0, animaciones=None, flip=False):
        self.animaciones = animaciones
        self.flip = flip

        self.nombre = nombre
        self.__nivel_fuerza = nivel_fuerza
        self.talla = talla
        self.planeta_origen = planeta_origen
        self.resistencia = resistencia
        self.x = x
        self.y = y

        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        self.image = animaciones[self.frame_index]
        #self.shape = pygame.Rect(self.x, self.y, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        self.shape = self.image.get_rect()
        self.shape.center = (self.x, self.y)
    
    def update(self, personaje2, animaciones_ataque, animaciones_perdida):
        coodown_animation = 200
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > coodown_animation:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0
        
        if personaje2.shape.colliderect(self.shape):
            #time.sleep(0.5)
            self.atacar(personaje2, animaciones_ataque)
            personaje2.mover(-50, 0)
            if personaje2.resistencia <= 0:
                print(f"{self.nombre} ha derrotado a {personaje2.nombre}!")
                personaje2.resistencia = 0
                personaje2.frame_index = 0
                personaje2.animaciones = animaciones_perdida
                self.frame_index = 0
                
        
    
    def dibujar(self, screen, forma = "cuadrado"):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(imagen_flip, self.shape)
        # if forma == "cuadrado":
        #pygame.draw.rect(screen, "blue", self.shape)
        # elif forma == "circulo":
        #     pygame.draw.circle(screen, "red", (self.x, self.y), 20)
    
    def mover(self, dx, dy):
        if dx < 0:
            self.flip = True
        elif dx > 0:
            self.flip = False

        self.shape.x += dx
        self.shape.y += dy
        #self.shape.center = (self.x, self.y)
    
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