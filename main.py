import os
import time
import asyncio
import threading
import multiprocessing
import random
import pygame
import constantes

from personajes import Personaje
from guerreros import Saiyajin, Guerrero, GuerreroProtocol, SaiyajinProtocol
from torneo import Torneo
from exceptions import ListadoNoEsListaException, ListadoVacioException

# goku = Saiyajin("Goku", 9001, 1.75, "Planeta Vegeta", cola=False, x=100, y=300)
# vegeta = Saiyajin("Vegeta", 8500, 1.65, "Planeta Vegeta", cola=True)
# krilin = Guerrero("Krilin", 3000, 1.50, "Tierra")
# picollo = Guerrero("Piccolo", 4000, 2.00, "Planeta Namek")
# yancha = Guerrero("Yamcha", 2500, 1.80, "Tierra")
# tenshinhan = Guerrero("Tenshinhan", 3200, 1.85, "Tierra")
# chaozu = Guerrero("Chaozu", 2800, 1.40, "Tierra")
# yajirobe = Guerrero("Yajirobe", 1500, 1.70, "Tierra")

# bulma = Personaje("Bulma", 500, 1.60, "Tierra")

# print(goku.saludar())
# print(goku.atacar())
# print(goku.nivel_fuerza)
# print(goku.transformarse_en_super_saiyajin())

#print(krilin.saludar())
#print(krilin.atacar())

#krilin.aumentar_fuerza()
#krilin.elevar_ki()
#gohan = Saiyajin.crear_saiyajin_terricola("Gohan", 5000, 1.80, cola=True)
#print(gohan.saludar())

#gothenks = Saiyajin.crear_saiyajin_terricola("Gotenks", 3900, 1.70, cola=False)
#print(gothenks.saludar())

#trunks = Saiyajin.crear_saiyajin_terricola("Trunks", 4500, 1.75, cola=False)
#print(trunks.saludar())

# rochi = Guerrero("Rochi", 2000, 1.60, "Tierra")
# broly = Saiyajin("Broly", 10000, 2.50, "Planeta Vegeta", cola=True)
# napa = Saiyajin("Napa", 7000, 1.90, "Planeta Vegeta", cola=True)
# raditz = Saiyajin("Raditz", 6000, 1.85, "Planeta Vegeta", cola=True)
# frezzer = Guerrero("Frezzer", 9900, 1.80, "Planeta Freezer")

#print(bulma.despedirse("¡Hasta luego!"))
#print(rochi.despedirse("¡Nos vemos en la próxima aventura!"))

#print(krilin.atacar())
# async def main():
#     torneo_dragon_ball = Torneo("¡Bienvenidos a las clasificatorias Torneo de Dragon Ball!", tipo=True)
#     print("Inicio de batallas sincronizadas:")
#     inicio_total = time.perf_counter()
#     resultados = await asyncio.gather(
#         torneo_dragon_ball.combate_clasificacion([goku, vegeta], 2),
#         torneo_dragon_ball.combate_clasificacion([broly, frezzer], 2),
#         torneo_dragon_ball.combate_clasificacion([gohan, krilin], 2),
#         torneo_dragon_ball.combate_clasificacion([trunks, picollo], 2)
#     )
#     fin_total = time.perf_counter()
#     print("\nResultados:", resultados)
#     print(f"Tiempo total de combates: {fin_total - inicio_total:.2f} segundos")
# asyncio.run(main())


# torneo_dragon_ball = Torneo("¡Bienvenidos a las clasificatorias Torneo de Dragon Ball!", tipo=True)
# t1 = threading.Thread(target=torneo_dragon_ball.combate_clasificacion, args=([goku, vegeta], 2))
# t2 = threading.Thread(target=torneo_dragon_ball.combate_clasificacion, args=([broly, frezzer], 2))

# print("Inicio de batallas con hilos:")
# inicio_total = time.perf_counter()
# t1.start()
# t2.start()

# t1.join()
# t2.join()
# fin_total = time.perf_counter()
# print(f"Tiempo total de combates con hilos: {fin_total - inicio_total:.2f} segundos")
# print("Combates de clasificación finalizados.")

# torneo_dragon_ball = Torneo("¡Bienvenidos a las clasificatorias Torneo de Dragon Ball!", tipo=True)
# p1 = multiprocessing.Process(target=torneo_dragon_ball.combate_clasificacion, args=([goku, vegeta], 2))
# p2 = multiprocessing.Process(target=torneo_dragon_ball.combate_clasificacion, args=([broly, frezzer], 2))

# print("Inicio de batallas con procesos:")
# inicio_total = time.perf_counter()
# p1.start()
# p2.start()

# p1.join()
# p2.join()
# fin_total = time.perf_counter()
# print(f"Tiempo total de combates con procesos: {fin_total - inicio_total:.2f} segundos")
# print("Combates de clasificación finalizados.")

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
def escalar_imagen(imagen, escala):
    ancho_nuevo = int(imagen.get_width() * escala)
    alto_nuevo = int(imagen.get_height() * escala)
    return pygame.transform.scale(imagen, (ancho_nuevo, alto_nuevo))

def contar_elementos(directorio):
    return len(os.listdir(directorio))
#print(f"Cantidad de elementos: {contar_elementos('assets/characters/personajes/freezer')}")
def nombres_carpetas(directorio):
    return os.listdir(directorio)
#print(f"Nombres de las carpetas: {nombres_carpetas('assets/characters/personajes')}")

pygame.init()
screen = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Torneo de Dragon Ball")
reloj = pygame.time.Clock()


directorio_personajes = "assets/characters/personajes"
tipo_personajes = nombres_carpetas(directorio_personajes)
animaciones = []
#animaciones_ataque_goku = []

for personaje in tipo_personajes:
    lista_temp = []
    ruta_temp = f"{directorio_personajes}/{personaje}"
    num_animaciones = contar_elementos(ruta_temp)
    print(f"Cantidad de animaciones para {personaje}: {num_animaciones}")
    for i in range(num_animaciones):
        imagen = pygame.image.load(f"{ruta_temp}/personaje_{i}.png").convert_alpha()
        imagen_escalada = escalar_imagen(imagen, 0.5)
        lista_temp.append(imagen_escalada)
    animaciones.append(lista_temp)


goku = Saiyajin("Goku", 990, 1.75, "Planeta Vegeta", cola=False, x=370, y=300, animaciones=animaciones[0][:len(animaciones[0]) - 3])

freezer = Guerrero("Freezer", 900, 1.80, "Planeta Freezer", x=420, y=300, animaciones=animaciones[1][:len(animaciones[1]) - 3], flip=True)

#definir las variables de movimiento del jugador


running = True
while running:
    reloj.tick(constantes.FPS)
    screen.fill(constantes.BG_COLOR)

    px_personaje1 = random.randint(-5, 5)
    py_personaje1 = random.randint(-5, 5)
    goku.mover(px_personaje1, py_personaje1)

    px_personaje2 = random.randint(-5, 5)
    py_personaje2 = random.randint(-5, 5)
    freezer.mover(px_personaje2, py_personaje2)

    #goku.mover(delta_x, delta_y)
    #freezer.mover(delta_x_freezer, delta_y_freezer)
    freezer.atacar(goku, animaciones[0][-3:])
    goku.atacar(freezer, animaciones[1][-3:])

    goku.update()
    freezer.update()
    
    goku.dibujar(screen)
    freezer.dibujar(screen)

    if goku.resistencia <= 0 or freezer.resistencia <= 0:
        print("¡Fin del combate!")
        time.sleep(2)
        running = False

    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        

    pygame.display.flip()

pygame.quit()