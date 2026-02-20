import random
from time import sleep
from exceptions import ListadoNoEsListaException, ListadoVacioException
from utilidades import medir_tiempo



def log_metodo(method):
    def wrapper(self, *args, **kwargs):
        print(f"Ejecutando método: {method.__name__}")
        sleep(1)  # Simula el tiempo de ejecución del método
        result = method(self, *args, **kwargs)
        print(f"Método {method.__name__} finalizado")
        return result
    return wrapper

# def filtrar_participantes(func):
#     def wrapper(self, *args, **kwargs):
#         print("Filtrando participantes con nivel de fuerza > 1000...")
#         if any(p.nivel_fuerza < 1000 for p in self.participantes):
#             raise ValueError("Todos los participantes deben tener un nivel de fuerza mayor a 1000.")
#         resultado = func(self, *args, **kwargs)
#         print("Filtrado completado.")
#         return resultado
#     return wrapper

class Torneo:
    def __init__(self, titulo, tipo=False):
        self.titulo = titulo
        self.tipo = tipo
        self.participantes = []
        self.batallas = []
        self.ganadores = []
        self.semifinalistas = []
        self.finalistas = []
    
    @log_metodo
    def listar_participantes(self):
        return [p for p in self.participantes if p.nivel_fuerza > 1000]
    

    def sortear_participantes(self, lista_filtrada):
        if not isinstance(lista_filtrada, list):
            raise ListadoNoEsListaException("El argumento proporcionado no es una lista.")
        if not lista_filtrada:
            raise ListadoVacioException("La lista proporcionada está vacía.")
        
        sleep(2)  # Simula el tiempo de preparación para el sorteo
        random.shuffle(lista_filtrada)

        def generar_combates():
            for index, participante in enumerate(lista_filtrada, start=1):
                print(f"{index}. {participante.nombre}")
                if index % 2 == 0:
                    combate = (lista_filtrada[index - 2], participante)
                    yield combate
        
        for num_combate, (p1, p2) in enumerate(generar_combates(), start=1):
            print(f"Sorteo Combate {num_combate}: {p1.nombre} vs {p2.nombre}")
            self.batallas.append((p1, p2))
            sleep(1)  # Simula el tiempo del sorteo de cada combate
        
    
    @medir_tiempo
    @staticmethod
    def preparar_combates():
        print("\nPreparando los combates del torneo...")
        sleep(2)  # Simula el tiempo de preparación para los combates

    def iniciar_torneo(self):
        print("\nIniciando batallas...")
        sleep(2)  # Simula el tiempo de preparación para los combates
        for combate in self.batallas:
            participante1, participante2 = combate
            print(f"\nCombate: {participante1.nombre} vs {participante2.nombre}")
            sleep(1)  # Simula el tiempo del combate
            
            print(participante1.atacar(participante2))
            print(participante2.atacar(participante1))
            while participante1.resistencia > 0 and participante2.resistencia > 0:
                print(participante1.atacar(participante2))
                print(participante2.atacar(participante1))
                sleep(1)  # Simula el tiempo entre ataques

            if participante1.resistencia > participante2.resistencia:
                print(f"Ganador: {participante1.nombre} con resistencia restante {participante1.resistencia}")
                print(f"Perdedor: {participante2.nombre} con resistencia restante {participante2.resistencia}")
                ganador = participante1
            elif participante2.resistencia > participante1.resistencia:
                print(f"Ganador: {participante2.nombre} con resistencia restante {participante2.resistencia}")
                print(f"Perdedor: {participante1.nombre} con resistencia restante {participante1.resistencia}")
                ganador = participante2
            else:
                print("Empate: No hay ganador")
                ganador = None
            
            if ganador:
                self.ganadores.append(ganador)
                print(f"{ganador.nombre} avanza a la siguiente ronda!")
            else:
                print(f"Empate entre {participante1.nombre} y {participante2.nombre}")
            
        print("\n-----------(Semifinalistas)-------------------")
        for index, ganador in enumerate(self.ganadores, start=1):
            self.semifinalistas.append(ganador)
            print(f"{index}. {ganador.nombre} - Nivel de Fuerza: {ganador.nivel_fuerza}")
        print("------------------------------")
        sleep(1)
        print("======= Iniciando Semifinales =======")
        sleep(2)
        for index, peleador in enumerate(self.semifinalistas, start=1):
            if index % 2 == 0:
                print(f"\nCombate Semifinal: {self.semifinalistas[index - 2].nombre} vs {peleador.nombre}")

                if (not self.tipo):
                    self.semifinalistas[index - 2].resistencia = 10000  # Reinicia la resistencia para la semifinal
                    peleador.resistencia = 10000  # Reinicia la resistencia para la semifinal

                print(self.semifinalistas[index - 2].atacar(peleador))
                print(peleador.atacar(self.semifinalistas[index - 2]))
                while self.semifinalistas[index - 2].resistencia > 0 and peleador.resistencia > 0:
                    print(self.semifinalistas[index - 2].atacar(peleador))
                    print(peleador.atacar(self.semifinalistas[index - 2]))
                    sleep(2)  # Simula el tiempo entre ataques
                
                if self.semifinalistas[index - 2].resistencia > peleador.resistencia:
                    print(f"Ganador Semifinal: {self.semifinalistas[index - 2].nombre} con resistencia restante {self.semifinalistas[index - 2].resistencia}")
                    print(f"Perdedor Semifinal: {peleador.nombre} con resistencia restante {peleador.resistencia}")
                    self.finalistas.append(self.semifinalistas[index - 2])
                elif peleador.resistencia > self.semifinalistas[index - 2].resistencia:
                    print(f"Ganador Semifinal: {peleador.nombre} con resistencia restante {peleador.resistencia}")
                    print(f"Perdedor Semifinal: {self.semifinalistas[index - 2].nombre} con resistencia restante {self.semifinalistas[index - 2].resistencia}")
                    self.finalistas.append(peleador)
                else:
                    print(f"Empate en Semifinal: {self.semifinalistas[index - 2].nombre} y {peleador.nombre}")
                    # En caso de empate, ambos avanzan a la final (opcional)
                    self.finalistas.append(self.semifinalistas[index - 2])
                    self.finalistas.append(peleador)    
                
        print("\n-------(Finalistas)-------------------")
        for index, finalista in enumerate(self.finalistas, start=1):
            print(f"{index}. {finalista.nombre} - Nivel de Fuerza: {finalista.nivel_fuerza}")
        print("---------------------------------------")
        print("===========Preparando Final===========")
        sleep(2)
        if len(self.finalistas) == 2:
            print(f"\nCombate Final: {self.finalistas[0].nombre} vs {self.finalistas[1].nombre}")
            sleep(2)  # Simula el tiempo del combate final
            
            if (not self.tipo):
                self.finalistas[0].resistencia = 10000  # Reinicia la resistencia para la final
                self.finalistas[1].resistencia = 10000  # Reinicia la resistencia

            print(self.finalistas[0].atacar(self.finalistas[1]))
            print(self.finalistas[1].atacar(self.finalistas[0]))
            while self.finalistas[0].resistencia > 0 and self.finalistas[1].resistencia > 0:
                print(self.finalistas[0].atacar(self.finalistas[1]))
                print(self.finalistas[1].atacar(self.finalistas[0]))
                sleep(2)  # Simula el tiempo entre ataques
            
            if self.finalistas[0].resistencia > self.finalistas[1].resistencia:
                print(f"\n¡El Gran Campeón del Torneo Dragon Ball es: {self.finalistas[0].nombre} con resistencia restante {self.finalistas[0].resistencia}!")
                print(f"Subcampeón: {self.finalistas[1].nombre} con resistencia restante {self.finalistas[1].resistencia}")
            elif self.finalistas[1].resistencia > self.finalistas[0].resistencia:
                print(f"\n¡El Gran Campeón del Torneo Dragon Ball es: {self.finalistas[1].nombre} con resistencia restante {self.finalistas[1].resistencia}!")
                print(f"Subcampeón: {self.finalistas[0].nombre} con resistencia restante {self.finalistas[0].resistencia}")
            else:                
                print("¡Empate en la final! No hay campeón.")
            
        else:
            print("No hay suficientes finalistas para el combate final o son muchos.")
        sleep(3)
        print("\nTorneo finalizado. Gracias por participar!")