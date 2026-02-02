import random

class Torneo:
    def __init__(self, titulo):
        self.titulo = titulo
        self.participantes = []
    
    def listar_participantes(self):
        return [p for p in self.participantes if p.get_nivel_fuerza() > 1000]
    

    def sortear_participantes(self, lista_filtrada):
        random.shuffle(lista_filtrada)
        for index, participante in enumerate(lista_filtrada, start=1):
            print(f"{index}. {participante.nombre}")
            if index % 2 == 0:
                print(f"combate {index // 2}: {lista_filtrada[index - 2].nombre} vs {participante.nombre}")