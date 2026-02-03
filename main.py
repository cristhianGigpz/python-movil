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

#print(goku.saludar())
#print(goku.atacar())
# print(goku.get_nivel_fuerza())
# print(goku.transformarse_en_super_saiyajin())

#print(krilin.saludar())
#print(krilin.atacar())

torneo_dragon_ball = Torneo("======Bienvenido al Torneo Dragon Ball 1======")
torneo_dragon_ball.participantes = [goku, vegeta, krilin, bulma, picollo, yancha, tenshinhan, chaozu, yajirobe]

print(torneo_dragon_ball.titulo)
print("Solo participantes con nivel de fuerza > 1000:")
lista_filtrada = torneo_dragon_ball.listar_participantes()
for participante in lista_filtrada:
    print(participante.nombre)
print("\nSorteo de participantes y combates:")
try:
    torneo_dragon_ball.sortear_participantes(lista_filtrada)
except (ListadoNoEsListaException, ListadoVacioException) as e:
    print(f"Error: {e}")

# litas_guerreros: list[SaiyajinProtocol] = [goku, vegeta, krilin, bulma]
# for guerrero in litas_guerreros:
#     print(guerrero.atacar())
# lista_personajes = [goku, vegeta, bulma]
# for personaje in lista_personajes:
#     print(personaje.saludar())

