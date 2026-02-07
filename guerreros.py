from abc import ABC, abstractmethod
from typing import Protocol
from personajes import Personaje

class GuerreroInterface(ABC):
    @abstractmethod
    def atacar(self) -> str:
        pass

    @abstractmethod
    def saludar(self) -> str:
        pass

    @abstractmethod
    def elevar_ki(self) -> str:
        pass

    def aumentar_fuerza(self):
        print("Aumentando la fueraza del guerrero!")
        self.elevar_ki()

class GuerreroProtocol(Protocol):
    def atacar(self) -> str:
        ...
    def saludar(self) -> str:
        ...

class SaiyajinProtocol(Protocol):
    def transformarse_en_super_saiyajin(self) -> str:
        ...
    def atacar(self) -> str:
        ...

class Saiyajin(Personaje):
    contador = 0
    def __init__(self, nombre, nivel_fuerza, talla, planeta_origen, cola = True):
        super().__init__(nombre, nivel_fuerza, talla, planeta_origen)
        self.cola = cola
        Saiyajin.contador += 1
    
    @classmethod
    def crear_saiyajin_terricola(cls, nombre, nivel_fuerza, talla, cola=False):
        return cls(nombre, nivel_fuerza, talla, "Tierra", cola=cola)

    def transformarse_en_super_saiyajin(self):
        nuevo_nivel = self.nivel_fuerza * 100
        self.nivel_fuerza = nuevo_nivel
        return f"{self.nombre} se ha transformado en Super Saiyajin! Nivel de fuerza: {self.nivel_fuerza}"

    def saludar(self):
        return f"Hola, soy {self.nombre} y soy un Saiyajin del planeta {self.planeta_origen}"
    
    def atacar(self):
        return f"{self.nombre} (saiyajin) está atacando con fuerza {self.nivel_fuerza}!"
    
    @classmethod
    def cantidad_saiyajines(cls):
        return cls.contador

class Guerrero(Personaje, GuerreroInterface):
    def __init__(self, nombre, nivel_fuerza, talla, planeta_origen):
        super().__init__(nombre, nivel_fuerza, talla, planeta_origen)
    
    def saludar(self):
        return f"Hola, soy {self.nombre} y soy un Guerrero"

    def atacar(self):
        return f"{self.nombre} está atacando con fuerza {self.nivel_fuerza}!"
    
    def elevar_ki(self):
        print(f"{self.nombre} ha elevado su ki!")