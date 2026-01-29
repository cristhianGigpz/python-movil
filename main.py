from personajes import Personaje

goku = Personaje("Goku", 9001)
# vegeta = Personaje("Vegeta", 8500)
# bulma = Personaje("Bulma", 10)

print(goku.saludar())
#goku._Personaje__nivel_fuerza = 500
goku.set_nivel_fuerza(500)
print(goku.get_nivel_fuerza())
# print(vegeta.saludar())
# print(bulma.saludar())