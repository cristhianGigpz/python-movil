import random
from exceptions import ListadoNoEsListaException, ListadoVacioException
from time import sleep
class Torneo:
    def __init__(self, titulo):
        self.titulo = titulo
        self.participantes = []
        self.batallas = []
        self.ganadores = []
    
    def listar_participantes(self):
        return [p for p in self.participantes if p.nivel_fuerza > 1000]
    

    def sortear_participantes(self, lista_filtrada):
        if not isinstance(lista_filtrada, list):
            raise ListadoNoEsListaException("El argumento proporcionado no es una lista.")
        if not lista_filtrada:
            raise ListadoVacioException("La lista proporcionada está vacía.")
        
        random.shuffle(lista_filtrada)
        for index, participante in enumerate(lista_filtrada, start=1):
            print(f"{index}. {participante.nombre}")
            if index % 2 == 0:
                self.batallas.append((lista_filtrada[index - 2], participante))
                print(f"combate {index // 2}: {lista_filtrada[index - 2].nombre} vs {participante.nombre}")
    
    @staticmethod
    def preparar_combates():
        print("Preparando los combates del torneo...")

    def iniciar_torneo(self):
        print("Iniciando batallas...")
        sleep(2)  # Simula el tiempo de preparación para los combates
        for combate in self.batallas:
            participante1, participante2 = combate
            print(f"\nCombate: {participante1.nombre} vs {participante2.nombre}")
            sleep(1)  # Simula el tiempo del combate
            if participante1.nivel_fuerza > participante2.nivel_fuerza:
                print(f"Ganador: {participante1.nombre}")
                ganador = participante1
            elif participante2.nivel_fuerza > participante1.nivel_fuerza:
                print(f"Ganador: {participante2.nombre}")
                ganador = participante2
            else:
                print("Empate: No hay ganador")
                ganador = None
            
            if ganador:
                self.ganadores.append(ganador)
                print(f"\n{ganador.nombre} avanza a la siguiente ronda!")
            else:
                print(f"\nEmpate entre {participante1.nombre} y {participante2.nombre}")
        print("------------------------------")
    
        