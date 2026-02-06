import random
from exceptions import ListadoNoEsListaException, ListadoVacioException

class Torneo:
    def __init__(self, titulo):
        self.titulo = titulo
        self.participantes = []
    
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
                print(f"combate {index // 2}: {lista_filtrada[index - 2].nombre} vs {participante.nombre}")
    
    @staticmethod
    def preparar_combates():
        print("Preparando los combates del torneo...")
        