from Constantes import *
from Funciones import *
import pygame


pygame.init()
pygame.display.set_caption("PREGUNTADOS")
icono = pygame.image.load("icono.png")

pantalla = pygame.display.set_mode(PANTALLA)
fondo_pantalla = pygame.transform.scale(pygame.image.load("fondo.jpg"),PANTALLA)

boton_volver = crear_elemento_juego("textura_respuesta.jpg",100,40,10,10)
boton_ranking = crear_elemento_juego("textura_pregunta.jpg",500,500,630,130)

def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],partidas:list) -> str:
    retorno = "rankings"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_volver["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "menu"

    pantalla.blit(fondo_pantalla,(0,0))
    pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])
    pantalla.blit(boton_ranking["superficie"],boton_ranking["rectangulo"])
    
    top_diez = ordenar_top(partidas)
    mostrar_top_10(top_diez,boton_ranking)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(2,-15),FUENTE_RESPUESTA_VOLVER,COLOR_BLANCO)
    
    return retorno

