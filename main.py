import time
from personajes import Personaje
from guerreros import Saiyajin, Guerrero, GuerreroProtocol, SaiyajinProtocol
from torneo import Torneo
from exceptions import ListadoNoEsListaException, ListadoVacioException

goku = Saiyajin("Goku", 9001, 1.75, "Planeta Vegeta", cola=False)
vegeta = Saiyajin("Vegeta", 8500, 1.65, "Planeta Vegeta", cola=True)
krilin = Guerrero("Krilin", 3000, 1.50, "Tierra")
picollo = Guerrero("Piccolo", 4000, 2.00, "Planeta Namek")
yancha = Guerrero("Yamcha", 2500, 1.80, "Tierra")
tenshinhan = Guerrero("Tenshinhan", 3200, 1.85, "Tierra")
chaozu = Guerrero("Chaozu", 2800, 1.40, "Tierra")
yajirobe = Guerrero("Yajirobe", 1500, 1.70, "Tierra")

bulma = Personaje("Bulma", 500, 1.60, "Tierra")

# print(goku.saludar())
# print(goku.atacar())
# print(goku.nivel_fuerza)
# print(goku.transformarse_en_super_saiyajin())

#print(krilin.saludar())
#print(krilin.atacar())

#krilin.aumentar_fuerza()
#krilin.elevar_ki()
gohan = Saiyajin.crear_saiyajin_terricola("Gohan", 5000, 1.80, cola=True)
#print(gohan.saludar())

gothenks = Saiyajin.crear_saiyajin_terricola("Gotenks", 3900, 1.70, cola=False)
#print(gothenks.saludar())

trunks = Saiyajin.crear_saiyajin_terricola("Trunks", 4500, 1.75, cola=False)
#print(trunks.saludar())

rochi = Guerrero("Rochi", 2000, 1.60, "Tierra")
broly = Saiyajin("Broly", 10000, 2.50, "Planeta Vegeta", cola=True)
napa = Saiyajin("Napa", 7000, 1.90, "Planeta Vegeta", cola=True)
raditz = Saiyajin("Raditz", 6000, 1.85, "Planeta Vegeta", cola=True)
frezzer = Guerrero("Frezzer", 9900, 1.80, "Planeta Freezer")

print(bulma.despedirse("¡Hasta luego!"))
print(rochi.despedirse("¡Nos vemos en la próxima aventura!"))

#print(krilin.atacar())
torneo_dragon_ball = Torneo("¡Bienvenidos a las clasificatorias Torneo de Dragon Ball!", tipo=True)
print("Inicio de batallas sincronizadas:")
inicio_total = time.perf_counter()
resultado1 = torneo_dragon_ball.combate_clasificacion([broly, frezzer], 2)
resultado2 = torneo_dragon_ball.combate_clasificacion([goku, vegeta], 2)
fin_total = time.perf_counter()
print(f"Resultados: {resultado1}, {resultado2}")
print(f"Tiempo total de combates: {fin_total - inicio_total:.2f} segundos")

# contador = 0
# while True:
#     respuesta = input("\n¿Quieres iniciar el juego? (s/n): ")
#     if respuesta.lower() == 'n':
#         print("¡Juego terminado!")
#         break
#     elif respuesta.lower() == 's':
#         print("¡Comenzando el juego!")
#         contador += 1

#         type_torneo = input("¿Quieres un torneo relampago? (s/n): ")
#         if type_torneo.lower() == 's':
#             tipo = True
#         else:
#             tipo = False

#         torneo_dragon_ball = Torneo(f"\n======Bienvenido al Torneo Dragon Ball {contador}======", tipo=tipo)

#         torneo_dragon_ball.participantes = [goku, vegeta, krilin, picollo, tenshinhan, gohan, gothenks, trunks, rochi, broly, napa, raditz, frezzer, yancha, chaozu, yajirobe, bulma]

#         print(torneo_dragon_ball.titulo)
#         print("Solo participantes con nivel de fuerza > 1000:")
#         lista_filtrada = torneo_dragon_ball.listar_participantes()

#         for participante in lista_filtrada:
#             print(participante.nombre)
#         print("\nSorteo de participantes y combates:")
#         try:
#             torneo_dragon_ball.sortear_participantes(lista_filtrada)
#         except (ListadoNoEsListaException, ListadoVacioException) as e:
#             print(f"Error: {e}")

#         # litas_guerreros: list[SaiyajinProtocol] = [goku, vegeta, krilin, bulma]
#         # for guerrero in litas_guerreros:
#         #     print(guerrero.atacar())
#         # lista_personajes = [goku, vegeta, bulma]
#         # for personaje in lista_personajes:
#         #     print(personaje.saludar())

#         Torneo.preparar_combates()
#         print(f"Cantidad de Saiyajines: {Saiyajin.cantidad_saiyajines()}")


#         torneo_dragon_ball.iniciar_torneo()

#     else:
#         print("Respuesta no válida. Por favor, ingresa 's' para sí o 'n' para no.")