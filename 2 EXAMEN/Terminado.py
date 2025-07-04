
from Constantes import *
from Funciones import *
import pygame
from datetime import date
import random


pygame.init()
pygame.display.set_caption("PREGUNTADOS")
icono = pygame.image.load("icono.png")
pantalla = pygame.display.set_mode(PANTALLA)
fondo_pantalla = pygame.transform.scale(pygame.image.load("fondo.jpg"), PANTALLA)
pygame.display.set_caption("Ingresar nombre")

boton_carga = crear_elemento_juego("textura_respuesta.jpg", ANCHO_BOTON_PREGUNTA, ALTO_BOTON_PREGUNTA, 670, 450)
def mostrar_fin_juego(pantalla: pygame.Surface, partidas, cola_eventos: list, datos_juegos: dict, texto: str = "") -> tuple:
    retorno = "terminado"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                datos_juegos["nombre"] = datos_juegos["nombre"][:-1]
            elif evento.key == pygame.K_RETURN or evento.key == 13:
                if len(datos_juegos["nombre"]) > 2 and es_alfabetico(datos_juegos["nombre"]):
                    partidas.append({
                        "nombre": datos_juegos["nombre"],
                        "puntuacion": datos_juegos["puntuacion"],
                        "dia": datos_juegos["fecha_hoy"]
                    })
                    guardar_puntuacion(partidas)
                    retorno = "menu"
            elif len(datos_juegos["nombre"]) < 10:
                tecla_presionada = pygame.key.name(evento.key)
                bloc_mayus = pygame.key.get_mods()

                if len(tecla_presionada) == 1:
                    if bloc_mayus >= 8192 or bloc_mayus == 1 or bloc_mayus == 2:
                        datos_juegos["nombre"] += tecla_presionada.upper()
                    else:
                        datos_juegos["nombre"] += tecla_presionada.lower()

    pantalla.blit(fondo_pantalla, (0, 0))

    limpiar_superficie(boton_carga, "textura_respuesta.jpg", ANCHO_BOTON_PREGUNTA, ALTO_BOTON_PREGUNTA)
    pantalla.blit(boton_carga["superficie"], boton_carga["rectangulo"])
    mostrar_texto(boton_carga["superficie"], f"Puntaje: {datos_juegos['puntuacion']} pts", (10, 10), FUENTE_RESPUESTA, COLOR_BLANCO)

    input_rect = pygame.Rect(140, 590, 800, 60)
    #pygame.draw.rect(pantalla, (255, 255, 255), input_rect, 2)


    nombre_ingresado = datos_juegos["nombre"]
    if nombre_ingresado == "":                                ## hacer funcion
        texto_mostrar = "Ingrese su nombre: "
    else:                                                          
        texto_mostrar = f"{nombre_ingresado}"

    fuente_input = pygame.font.SysFont(FUENTE_JUEGO, 40, True)
    mostrar_texto(pantalla, texto_mostrar, (720, 470), fuente_input, COLOR_NEGRO)

    return retorno, texto

# # # # def mostrar_fin_juego(pantalla: pygame.surface, partidas, cola_eventos: list, datos_juegos: dict, texto: str = "") -> tuple:
# # # #     retorno = "terminado"

# # # #     for evento in cola_eventos:
# # # #         if evento.type == pygame.KEYDOWN:
# # # #             tecla_presionada = pygame.key.name(evento.key)
# # # #             bloc_mayus = pygame.key.get_mods()

# # # #             if evento.key == pygame.K_BACKSPACE:
# # # #                 datos_juegos["nombre"] = datos_juegos["nombre"][:-1]
# # # #             elif evento.key == pygame.K_RETURN:
# # # #                 if len(datos_juegos["nombre"]) > 2 and datos_juegos["nombre"].isalpha():
# # # #                     partidas.append({
# # # #                         "nombre": datos_juegos["nombre"],
# # # #                         "puntuacion": datos_juegos["puntuacion"],
# # # #                         "dia": datos_juegos["fecha_hoy"]
# # # #                     })
# # # #                     guardar_puntuacion(partidas)
# # # #                     retorno = "menu"
# # # #             elif len(tecla_presionada) == 1:
# # # #                 if bloc_mayus >= 8192 or bloc_mayus == 1 or bloc_mayus == 2:
# # # #                     datos_juegos["nombre"] += tecla_presionada.upper()
# # # #                 else:
# # # #                     datos_juegos["nombre"] += tecla_presionada.lower()

# # # #     # Dibujar fondo
# # # #     pantalla.blit(fondo_pantalla, (0, 0))

# # # #     # Botón donde se muestra el puntaje (no se usa más como input)
# # # #     limpiar_superficie(boton_carga, "textura_respuesta.jpg", ANCHO_BOTON_PREGUNTA, ALTO_BOTON_PREGUNTA)
# # # #     pantalla.blit(boton_carga["superficie"], boton_carga["rectangulo"])
# # # #     mostrar_texto(boton_carga["superficie"], f"Puntaje: {datos_juegos['puntuacion']} pts", (10, 10), FUENTE_RESPUESTA, COLOR_BLANCO)

# # # #     # Dibujar caja blanca para entrada de nombre
# # # #     input_rect = pygame.Rect(140, 590, 800, 60)
# # # #     pygame.draw.rect(pantalla, (255, 255, 255), input_rect, 2)  # borde blanco

# # # #     # Mostrar texto del nombre ingresado o mensaje
# # # #     nombre_ingresado = datos_juegos["nombre"]
# # # #     if nombre_ingresado == "":
# # # #         texto_mostrar = "Ingrese su nombre:"
# # # #     else:
# # # #         texto_mostrar = f"Nombre: {nombre_ingresado}_"

# # # #     # Fuente más clara para el input
# # # #     fuente_input = pygame.font.SysFont("Arial", 40, True)
# # # #     mostrar_texto(pantalla, texto_mostrar, (150, 600), fuente_input, COLOR_NEGRO)

# # # #     return retorno, texto

# from Constantes import *
# from Funciones import *
# import pygame
# from datetime import date
# import copy

# pygame.init()
# pygame.display.set_caption("PREGUNTADOS")
# icono = pygame.image.load("icono.png")

# pantalla = pygame.display.set_mode(PANTALLA)
# fondo_pantalla = pygame.transform.scale(pygame.image.load("fondo.jpg"),PANTALLA)
# pygame.display.set_caption("Ingresar nombre")

# corriendo = True
# reloj = pygame.time.Clock()
# evento_tiempo = pygame.USEREVENT
# pygame.time.set_timer(evento_tiempo,1000)
# escribiendo = True

# boton_carga = crear_elemento_juego("textura_respuesta.jpg", ANCHO_BOTON_PREGUNTA, ALTO_BOTON_PREGUNTA, 150,500)

# #def mostrar_fin_juego(pantalla:pygame.surface,partidas, cola_eventos:list, datos_juegos:dict, texto:str = "", partidas:list) -> bool:


# def mostrar_fin_juego(pantalla:pygame.surface,partidas, cola_eventos:list, datos_juegos:dict, texto:str = "") -> bool:
#     retorno = "terminado"
#     for evento in cola_eventos:
#             # if evento.type == pygame.QUIT:
#             #     retorno = "salir"
#     # # if evento.key == pygame.K_RETURN or len(texto) > 20:
#             if evento.type == pygame.KEYDOWN:
#                 limpiar_superficie(boton_carga, "textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA, ALTO_BOTON_PREGUNTA)
#                 tecla_presionada = pygame.key.name(evento.key)
#                 bloc_mayus = pygame.key.get_mod()
                
#                 print(evento.key)
#                 if evento.key > 0 and evento.key < 256: #EVENTOS POR CHR
#                     caracter = chr(evento.key)
#                     print(caracter)
                
                
#                 print(tecla_presionada) #LETRA muestra
                
#                 if tecla_presionada == "backspace":
#                 #elif len(tecla_presionada) == "backspace":
#                     datos_juegos["nombre"] =  datos_juegos["nombre"][0:len(datos_juegos["nombre"]) - 1] #devuelve cadena del indice 0 menos la última
#                     datos_juegos["nombre"] += ""
                
#                 elif len(tecla_presionada) == 1:
#                     #manipula el bloc mayus y el shift izq/der para hacer mayus
#                     if bloc_mayus >= 8192 or bloc_mayus == 1 or bloc_mayus == 2:
#                         datos_juegos["nombre"] += tecla_presionada.upper()
#                     else:
#                         datos_juegos["nombre"] += tecla_presionada
                    
                
                    
#                 elif tecla_presionada == "return":
#                     #GUARDA LA PUNTUACIÓN AL RANKING
#                     #lista_rankings.append(puntuacion)
#                     #actualizar aca el json
                    
#                     #reiniciar_estadisticas(datos_juego[""])
                    
#                     retorno = "menu"
                    

#                 datos_juegos["nombre"] += caracter
#                 print(datos_juegos["nombre"]) #VALOR ASCII LETRA muestra
                
#                 # # if evento.key == pygame.K_RETURN or len(texto) > 20:
#                 # #     if len(texto) > 2 and texto.isalpha():  
#                 # #         datos_juegos["nombre"] = texto
#                 # #         partidas.append({
#                 # #         "nombre": datos_juegos["nombre"],
#                 # #         "puntuacion": datos_juegos["puntuacion"],
#                 # #         "dia": datos_juegos["fecha_hoy"]})

#                 # #         guardar_puntuacion(partidas)
#                 # #         retorno = "menu"
#                 # #     else:
#                 # #             pass
#                 # # elif evento.key == pygame.K_BACKSPACE:
#                 # #     texto = texto[:-1]
#                 # # else:
#                 # #     texto += evento.unicode
                                     
#     pantalla.blit(fondo_pantalla,(0,0))
#     pantalla.blit(boton_carga["superficie"],boton_carga["rectangulo"])
#     #mostrar_texto(boton_carga["superficie"],"Ingrese su nombre",(5,5),FUENTE_RESPUESTA,"#727272")

#     mostrar_texto(boton_carga["superficie"], f"Usted obtuvo: {datos_juegos["puntuacion"]} puntos", (250,100), FUENTE_PREGUNTA)

# #    mostrar_texto(boton_carga,f"Usted obtuvo: {datos_juegos["puntuacion"]} puntos",(250,100),FUENTE_PREGUNTA)
    
#     mostrar_texto(boton_carga["superficie"], datos_juegos["nombre"], (250,100), FUENTE_RESPUESTA, COLOR_BLANCO)
    
    
#     if datos_juegos["nombre"] != "":
#         limpiar_superficie(boton_carga, "textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA, ALTO_BOTON_PREGUNTA)

#         mostrar_texto(boton_carga["superficie"], datos_juegos["nombre"], (250,100), FUENTE_RESPUESTA, COLOR_BLANCO)


        
#         if random.randint(1,2) == 1:
#             mostrar_texto(boton_carga["superficie"], f"{datos_juegos["nombre"]}|", (250,100), FUENTE_RESPUESTA, COLOR_BLANCO)


#     else:
#         limpiar_superficie(boton_carga, "textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA, ALTO_BOTON_PREGUNTA)

#         mostrar_texto(boton_carga["superficie"], "Ingrese su nombre: ", (250,100), FUENTE_RESPUESTA, "#613838")
        

    
#     return retorno,texto
    


# # from Constantes import *
# # from Funciones import *
# # import pygame
# # from datetime import date
# # import copy

# # pygame.init()
# # pygame.display.set_caption("PREGUNTADOS")
# # icono = pygame.image.load("icono.png")

# # pantalla = pygame.display.set_mode(PANTALLA)
# # fondo_pantalla = pygame.transform.scale(pygame.image.load("fondo.jpg"),PANTALLA)
# # pygame.display.set_caption("Ingresar nombre")

# # corriendo = True
# # reloj = pygame.time.Clock()
# # evento_tiempo = pygame.USEREVENT
# # pygame.time.set_timer(evento_tiempo,1000)
# # escribiendo = True


# # boton_carga = crear_elemento_juego("textura_respuesta.jpg", ANCHO_BOTON_PREGUNTA, ALTO_BOTON_PREGUNTA, 150, 500,)

# # def mostrar_fin_juego(pantalla:pygame.surface,partidas, cola_eventos:list, datos_juegos:dict, texto:str = "") -> bool:
# #     retorno = "terminado"
# #     for evento in cola_eventos:
# #             if evento.type == pygame.QUIT:
# #                 retorno = "salir"
# #             elif evento.type == pygame.KEYDOWN:
# #                     if evento.key == pygame.K_RETURN or len(texto) > 20:
# #                             if len(texto) > 2 and texto.isalpha():  
# #                                 datos_juegos["nombre"] = texto
# #                                 partidas.append({
# #                                 "nombre": datos_juegos["nombre"],
# #                                 "puntuacion": datos_juegos["puntuacion"],
# #                                 "dia": datos_juegos["fecha_hoy"]})

# #                                 guardar_puntuacion(partidas)
# #                                 retorno = "menu"
# #                             else:
# #                                   pass
# #                     elif evento.key == pygame.K_BACKSPACE:
# #                         texto = texto[:-1]
# #                     else:
# #                         texto += evento.unicode
                                     
# #     pantalla.blit(fondo_pantalla,(0,0))
# #     pantalla.blit(boton_carga["superficie"],boton_carga["rectangulo"])

# #     mostrar_texto(boton_carga["superficie"],"Ingrese su nombre",(5,5),FUENTE_RESPUESTA,"#727272")
    
# #     return retorno,texto
    
