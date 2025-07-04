import pygame 
from Constantes import *
from Menu import *
from Juego import *
from Configuracion import *
from Rankings import *
from Terminado import *
from datetime import date

pygame.init()
pygame.display.set_caption("PREGUNTADOS")
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)
pantalla = pygame.display.set_mode(PANTALLA)
pygame.mixer.init()
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1)



datos_juego = {
    "puntuacion":0,
    "vidas":CANTIDAD_VIDAS,
    "nombre":"","r_correctas_seguidas":0,
    "tiempo_restante":30,
    "indice":0,
    "volumen_musica":100,
    "fecha_hoy":str(date.today()),
    "bandera_c_bomba": False,           # Bomba: Elimina dos respuestas incorrectas
    "bandera_c_por_2": False,           # X2: Duplica puntos de la respuesta actual
    "bandera_c_doble_chance": False,    # Doble chance: Permite 2 intentos en una pregunta
    "bandera_c_pasar": False,
    "modo_doble_chance": False,
    "intento_doble_chance": False,
    "aplicar_x2": False
    }

partidas = [
]

corriendo = True
texto = ""
reloj = pygame.time.Clock()
bandera_musica = False
bandera_juego = False

ventana_actual = "menu" #VENTANA POR DEFECTO / LAS CAMBIA SEGÚN REQUIERA MOSTRAR

while corriendo:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get() #EJECUTA NUEVA COLA DE EVENTOS
    
    if ventana_actual == "menu":
        if bandera_musica == True:
            pygame.mixer.music.stop()
            bandera_musica = False
        if bandera_juego == True:
            texto = limpiar_string(texto)
            reiniciar_estadisticas(datos_juego)
            bandera_juego = False
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "terminado":
         ventana_actual,texto = mostrar_fin_juego(pantalla, partidas ,cola_eventos, datos_juego,texto)
    elif ventana_actual == "juego":
       
        bandera_juego = True
        porcentaje_volumen = datos_juego["volumen_musica"] / 100

        if bandera_musica == False:
            pygame.mixer.music.load("musica.mp3")
            pygame.mixer.music.set_volume(porcentaje_volumen)
            pygame.mixer.music.play(-1)
            bandera_musica = True
            
       

        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "salir":
        corriendo = False
    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_ajustes(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos,partidas)
    pygame.display.flip()

pygame.quit()
    
                        