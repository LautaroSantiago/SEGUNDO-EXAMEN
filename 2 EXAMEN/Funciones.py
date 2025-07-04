import random
from Constantes import *
import pygame
import json
import copy
import os

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

#GENERAL
def mezclar_lista(lista_preguntas:list) -> None:
    random.shuffle(lista_preguntas)

#GENERAL
def reiniciar_estadisticas(datos_juego:dict) -> None:
    datos_juego["puntuacion"] = 0
    datos_juego["vidas"] = CANTIDAD_VIDAS
    datos_juego["nombre"] = ""
    datos_juego["tiempo_restante"] = 30

#GENERAL
def verificar_respuesta(datos_juego:dict,pregunta:dict,respuesta:int) -> bool:
    if respuesta == pregunta["respuesta_correcta"]:
        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
        retorno = True
    else:
        if datos_juego["puntuacion"] > 0:
            datos_juego["puntuacion"] -= PUNTUACION_ERROR
        datos_juego["vidas"] -= 1
        retorno = False 

        
    return retorno

def crear_elemento_juego(textura:str,ancho:int,alto:int,pos_x:int,pos_y:int) -> dict:
    elemento_juego = {}
    elemento_juego["superficie"] = pygame.transform.scale(pygame.image.load(textura),(ancho,alto))
    elemento_juego["rectangulo"] = elemento_juego["superficie"].get_rect()
    elemento_juego["rectangulo"].x = pos_x
    elemento_juego["rectangulo"].y = pos_y
    
    return elemento_juego

def limpiar_superficie(elemento_juego:dict,textura:str,ancho:int,alto:int) -> None:
    elemento_juego["superficie"] =  pygame.transform.scale(pygame.image.load(textura),(ancho,alto))
    
def obtener_respuesta_click(boton_respuesta_uno:dict,boton_respuesta_dos:dict,boton_respuesta_tres:dict,boton_respuesta_cuatro:dict,pos_click:tuple):
    lista_aux = [boton_respuesta_uno["rectangulo"],boton_respuesta_dos["rectangulo"],boton_respuesta_tres["rectangulo"], boton_respuesta_cuatro["rectangulo"]]
    respuesta = None
    
    for i in range(len(lista_aux)):
        if lista_aux[i].collidepoint(pos_click):
            respuesta = i + 1
    
    return respuesta

def cambiar_pregunta(lista_preguntas:list,indice:int,caja_pregunta:dict,boton_respuesta_uno:dict,boton_respuesta_dos:dict,boton_respuesta_tres:dict,boton_respuesta_cuatro:dict) -> dict:
    pregunta_actual = lista_preguntas[indice]
    limpiar_superficie(caja_pregunta,"textura_pregunta.jpg",ANCHO_PREGUNTA,ALTO_PREGUNTA)
    limpiar_superficie(boton_respuesta_uno,"textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA)
    limpiar_superficie(boton_respuesta_dos,"textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA)
    limpiar_superficie(boton_respuesta_tres,"textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA)
    limpiar_superficie(boton_respuesta_cuatro,"textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA) 

    return pregunta_actual

def crear_botones_menu() -> list:
    lista_botones = []
    pos_y = 135

    for i in range(4):
        boton = crear_elemento_juego("textura_respuesta.jpg",ANCHO_BOTON,ALTO_BOTON,570,pos_y)
        pos_y += 130
        lista_botones.append(boton)
        
    return lista_botones


def guardar_puntuacion(datos: list)-> None:
   with open("partidas.json", 'w') as partidas:
    json.dump(datos,partidas, indent = 4)

def limpiar_string(texto:str) -> str:
    return ""

def limpiar_diccionario(diccionario:dict) -> str:
    return ""


# def mostrar_top(partidas:list)->None:
#     top_10 = ordenar_top(partidas)
#     for key,value in top_10.items():
#         print(f"{key}:{value}")




def ordenar_top(partidas:list)-> list:
    lista_ordenada = sorted(partidas, key=lambda x: x["puntuacion"], reverse=True)
    top_diez = lista_ordenada[0:10]


    return top_diez
 
# def ingresar_mostrar_nombre(nombre: str, texto_mostrar:str) -> None:
#     nombre_ingresado = nombre
#     if nombre_ingresado == "":
#         texto_mostrar = "Ingrese su nombre:"
#     else:
#         texto_mostrar = f"{nombre_ingresado}"
    
#     return texto_mostrar
    

#Especifica
def leer_csv_preguntas(nombre_archivo:str,lista_preguntas:list,separador:str = ",") -> bool:
    if os.path.exists(nombre_archivo) == True:
        with open(nombre_archivo,"r", encoding="utf-8") as archivo:
            #Falsa lectura --> Una lectura fantasma, para evitar que cuando se recorra con el for de abajo me muestre la cabecera
            archivo.readline()
            
            for linea in archivo:
                preguntas = crear_diccionario_preguntas(linea,separador)
                lista_preguntas.append(preguntas)
        
        retorno = True
    else:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
        retorno = False
        
    return retorno

#ESPECIFICA

def crear_diccionario_preguntas(linea:str,separador:str = ",") -> dict:
    linea = linea.replace("","")
    lista_valores = linea.split(separador)
    
    preguntas = {}
    preguntas["pregunta"] = lista_valores[0]
    preguntas["respuesta_1"] = lista_valores[1]
    preguntas["respuesta_2"] = lista_valores[2]
    preguntas["respuesta_3"] = lista_valores[3]
    preguntas["respuesta_4"] = lista_valores[4]
    preguntas["respuesta_correcta"] = int(lista_valores[5])
    preguntas["dificultad"] = lista_valores[6]
    
    return preguntas

#from funciones_csv import leer_csv_preguntas  # Asegurate de importar correctamente directamente copiar las funciones en tu archivo principal si es más simple

# lista_preguntas = []

# ruta_archivo = "preguntas.csv"  # O la ruta real
# print(f"Buscando archivo en: {ruta_archivo}")
# if leer_csv_preguntas(ruta_archivo, lista_preguntas):
#     print("Preguntas cargadas exitosamente.")
#     print(lista_preguntas[0])  # Mostramos la primera para chequear
# else:
#     print("No se pudo cargar el archivo.")

def es_alfabetico(cadena:str) -> bool:
    """Verifica si una cadena contiene únicamente letras y espacios.

    Args:
        cadena (str): Cadena de caracteres a validar.

    Returns:
        bool: True si la cadena es alfabética (letras y espacios)
    """
    if len(cadena) > 0:
        retorno = True
     
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])

            if (valor_ascii > 90 or valor_ascii < 65) and (valor_ascii > 
            122 or valor_ascii < 97) and valor_ascii != 32:
                retorno = False
                break
    else:
        retorno = False

    return retorno


def eliminar_dos_incorrectas(pregunta):
    respuestas = ["respuesta_1", "respuesta_2", "respuesta_3", "respuesta_4"]
    correct = pregunta["respuesta_correcta"]  # Número de la correcta, por ej. 1
    incorrectas = [r for r in respuestas if r[-1] != str(correct)]
    a_ocultar = random.sample(incorrectas, 2)
    for r in a_ocultar:
        pregunta[r] = ""  # O podés poner "----" o algo visual

def mostrar_top_10(top_diez:list,boton_ranking:dict) -> None:
# Mostrar cada línea del ranking
    y_pos = 50
    i = 1
    for entrada in top_diez:
        texto = f"{i}. {entrada['nombre']} - {entrada['puntuacion']} pts"
        texto_2 = f"Fecha: {entrada['dia']}"
        mostrar_texto(boton_ranking["superficie"], texto, (50, y_pos), FUENTE_TOP_10, COLOR_NEGRO)
        y_pos += 40
        mostrar_texto(boton_ranking["superficie"], texto_2, (50, y_pos), FUENTE_TOP_10, COLOR_NEGRO)
        y_pos += 40
        i += 1

def verificar_respuesta_por_dos(datos_juego:dict,pregunta_actual:dict,respuesta:int, puntos_a_sumar:int) -> None:
    
    

    if respuesta == pregunta_actual["respuesta_correcta"]:
        puntos_a_sumar *= 2
        datos_juego["puntuacion"] += puntos_a_sumar
        retorno = True
    else:
        if datos_juego["puntuacion"] > 0:
            datos_juego["puntuacion"] -= PUNTUACION_ERROR
        datos_juego["vidas"] -= 1
    

        retorno = False 
    datos_juego["aplicar_x2"] = False  # se consume
    return retorno