from personajes import Personaje
from guerreros import Saiyajin, Guerrero, GuerreroProtocol, SaiyajinProtocol

goku = Saiyajin("Goku", 9001, 1.75, "Planeta Vegeta", cola=False)
vegeta = Saiyajin("Vegeta", 8500, 1.65, "Planeta Vegeta", cola=True)
krilin = Guerrero("Krilin", 3000, 1.50, "Tierra")

bulma = Personaje("Bulma", 500, 1.60, "Tierra")

print(goku.saludar())
print(goku.atacar())
# print(goku.get_nivel_fuerza())
# print(goku.transformarse_en_super_saiyajin())

print(krilin.saludar())
print(krilin.atacar())

litas_guerreros: list[SaiyajinProtocol] = [goku, vegeta, krilin, bulma]
for guerrero in litas_guerreros:
    print(guerrero.atacar())
# lista_personajes = [goku, vegeta, bulma]
# for personaje in lista_personajes:
#     print(personaje.saludar())

