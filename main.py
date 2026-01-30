from personajes import Personaje
from saiyajines import Saiyajin

goku = Saiyajin("Goku", 9001, 1.75, "Planeta Vegeta", cola=False)
vegeta = Saiyajin("Vegeta", 8500, 1.65, "Planeta Vegeta", cola=True)

bulma = Personaje("Bulma", 500, 1.60, "Tierra")

print(goku.saludar())
print(goku.get_nivel_fuerza())
print(goku.transformarse_en_super_saiyajin())

lista_personajes = [goku, vegeta, bulma]
for personaje in lista_personajes:
    print(personaje.saludar())

