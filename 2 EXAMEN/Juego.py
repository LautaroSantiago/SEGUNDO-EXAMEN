import pygame
from Constantes import *
#from Preguntas import *
from Funciones import *
from datetime import date


pygame.init()

pygame.display.set_caption("PREGUNTADOS")
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)

pantalla = pygame.display.set_mode(PANTALLA)

datos_juego = {
    "puntuacion":0,
    "vidas":CANTIDAD_VIDAS,
    "nombre":"","r_correctas_seguidas":0,
    "tiempo_restante":30,
    "indice":0,
    "volumen_musica":100,
    "fecha_hoy":str(date.today()),
    "bandera_c_bomba": False,           # Bomba: Elimina dos respuestas incorrectas
    "bandera_c_por_2": False,
    "bandera_respuesta_respondida":0,           # X2: Duplica puntos de la respuesta actual
    "bandera_c_doble_chance": False,    # Doble chance: Permite 2 intentos en una pregunta
    "bandera_c_pasar": False, 
    "modo_doble_chance": False,
    "intento_doble_chance": False,
    "aplicar_x2": False
    }

# datos_juego = {
#     "puntuacion":0,
#     "vidas":CANTIDAD_VIDAS,
#     "nombre":"",
#     "tiempo_restante":30,
#     "indice":0,
#     "volumen_musica":100,
#     "fecha_hoy":str(date.today()), 
#     "bandera_c_bomba": False,
#     "bandera_c_por_2":False, 
#     "bandera_c_doble_chance":False,
#     "bandera_c_pasar": False}

fondo_pantalla = pygame.transform.scale(pygame.image.load("fondo.jpg"),PANTALLA)

#Elemento del juego
caja_pregunta = crear_elemento_juego("textura_pregunta.jpg",ANCHO_PREGUNTA,ALTO_PREGUNTA,700,125)
boton_respuesta_uno = crear_elemento_juego("textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA,450,400)
boton_respuesta_dos = crear_elemento_juego("textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA,900,400)
boton_respuesta_tres = crear_elemento_juego("textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA,450,500)
boton_respuesta_cuatro = crear_elemento_juego("textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA,900,500)
corazon_vida_uno = crear_elemento_juego("corazon_vida.jpg",ANCH0_CORAZON,ALTO_CORAZON,415,125)

boton_bomba = crear_elemento_juego("BOMBA.png",ANCH0_BOTON_BONUS,ALTO_BOTON_BONUS,100,37)
boton_duplicar = crear_elemento_juego("DUPLICAR.png",ANCH0_BOTON_BONUS,ALTO_BOTON_BONUS,100,225)
boton_por_dos = crear_elemento_juego("X2.png",ALTO_BOTON_BONUS,ALTO_BOTON_BONUS,100,406)
boton_pasar = crear_elemento_juego("PASAR.png",ALTO_BOTON_BONUS,ALTO_BOTON_BONUS,100,590)

pygame.draw.rect(pantalla, (255,0,0), boton_bomba["rectangulo"], 2)
pygame.draw.rect(pantalla, (0,255,0), boton_duplicar["rectangulo"], 2)
pygame.draw.rect(pantalla, (0,0,255), boton_por_dos["rectangulo"], 2)
pygame.draw.rect(pantalla, (255,255,0), boton_pasar["rectangulo"], 2)

lista_preguntas = []
ruta_archivo = "preguntas.csv"

if not leer_csv_preguntas(ruta_archivo, lista_preguntas):
    exit()


mezclar_lista(lista_preguntas)

corriendo = True
reloj = pygame.time.Clock()
evento_tiempo = pygame.USEREVENT
pygame.time.set_timer(evento_tiempo,1000)

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "juego"
    pregunta_actual = lista_preguntas[datos_juego['indice']]
    
    if datos_juego["vidas"] == 0 or datos_juego["tiempo_restante"] == 0:
        retorno = "terminado"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                respuesta = obtener_respuesta_click(boton_respuesta_uno,boton_respuesta_dos,boton_respuesta_tres,boton_respuesta_cuatro,evento.pos)
                if respuesta != None:
                    if verificar_respuesta(datos_juego,pregunta_actual,respuesta) == True:
                            #Recomiendo sonido de respuesta correcta
                            CLICK_SONIDO.play()
                            datos_juego["r_correctas_seguidas"] += 1 
                            

                            if datos_juego.get("aplicar_x2"):
                                puntos_a_sumar = PUNTUACION_ACIERTO
                                if verificar_respuesta_por_dos(datos_juego,pregunta_actual,respuesta,puntos_a_sumar) == True: 
                                    datos_juego["r_correctas_seguidas"] += 1    
                            
                    else:
                        datos_juego["r_correctas_seguidas"] = 0
                        ERROR_SONIDO.play()

                    if datos_juego["r_correctas_seguidas"] == 5: #Si responde correctamente 5 veces seguidas gana una vida.
                        datos_juego["vidas"] += 1
                        datos_juego["tiempo_restante"] += 10
                        datos_juego["r_correctas_seguidas"] = 0
                    datos_juego['indice'] += 1
                    if datos_juego['indice'] == len(lista_preguntas):
                        mezclar_lista(lista_preguntas)
                        datos_juego['indice'] = 0
                    pregunta_actual = cambiar_pregunta(lista_preguntas,datos_juego['indice'],caja_pregunta,boton_respuesta_uno,boton_respuesta_dos,boton_respuesta_tres,boton_respuesta_cuatro)    

                if boton_pasar["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    if not datos_juego["bandera_c_pasar"]:
                        datos_juego["bandera_c_pasar"] = True
                        datos_juego['indice'] 
                        datos_juego['indice'] += 1
                        if datos_juego['indice'] == len(lista_preguntas):
                            mezclar_lista(lista_preguntas)
                            datos_juego['indice'] = 0                        
                    pregunta_actual = cambiar_pregunta(lista_preguntas,datos_juego['indice'],caja_pregunta,boton_respuesta_uno,boton_respuesta_dos,boton_respuesta_tres,boton_respuesta_cuatro)    
                
                if boton_por_dos["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    if not datos_juego["bandera_c_por_2"]:
                        datos_juego["bandera_c_por_2"] = True
                        datos_juego["aplicar_x2"] = True
                        puntos_a_sumar = PUNTUACION_ACIERTO

        elif evento.type == evento_tiempo:
            datos_juego["tiempo_restante"] -= 1

    pantalla.blit(fondo_pantalla,(0,0))
    pantalla.blit(caja_pregunta["superficie"],caja_pregunta["rectangulo"])
    pantalla.blit(boton_respuesta_uno["superficie"],boton_respuesta_uno["rectangulo"])
    pantalla.blit(boton_respuesta_dos["superficie"],boton_respuesta_dos["rectangulo"])
    pantalla.blit(boton_respuesta_tres["superficie"],boton_respuesta_tres["rectangulo"])
    pantalla.blit(boton_respuesta_cuatro["superficie"],boton_respuesta_cuatro["rectangulo"])
    pantalla.blit(corazon_vida_uno["superficie"],corazon_vida_uno["rectangulo"])
    
    pantalla.blit(boton_bomba["superficie"],boton_bomba["rectangulo"])
    pantalla.blit(boton_duplicar["superficie"],boton_duplicar["rectangulo"])
    pantalla.blit(boton_por_dos["superficie"],boton_por_dos["rectangulo"])
    pantalla.blit(boton_pasar["superficie"],boton_pasar["rectangulo"])
    

    mostrar_texto(caja_pregunta["superficie"],pregunta_actual["pregunta"],(20,10),FUENTE_PREGUNTA,COLOR_NEGRO)
    mostrar_texto(boton_respuesta_uno["superficie"],pregunta_actual["respuesta_1"],(20,20),FUENTE_RESPUESTA,COLOR_BLANCO)
    mostrar_texto(boton_respuesta_dos["superficie"],pregunta_actual["respuesta_2"],(20,20),FUENTE_RESPUESTA,COLOR_BLANCO)
    mostrar_texto(boton_respuesta_tres["superficie"],pregunta_actual["respuesta_3"],(20,20),FUENTE_RESPUESTA,COLOR_BLANCO)
    mostrar_texto(boton_respuesta_cuatro["superficie"],pregunta_actual["respuesta_4"],(20,20),FUENTE_RESPUESTA,COLOR_BLANCO)

    mostrar_texto(pantalla,f"{datos_juego['vidas']}",(475,130),FUENTE_DATOS,COLOR_ROJO)
    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(415,195),FUENTE_DATOS_PUNTUACION)
    mostrar_texto(pantalla,f"TIEMPO: {datos_juego['tiempo_restante']} s",(1050,125),FUENTE_DATOS)

    return retorno

