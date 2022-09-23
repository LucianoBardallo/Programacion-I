import re
import json

#from Clase_4.Ejercicio7 import *

def imprimir_dato(dato:str):
    '''
    Imprime un dato del tipo string pasado por parametro
    '''
    print(dato)

#---------------------PUNTO 1----------------

#1.1
def imprimir_menu_desafio_5():
    imprimir_dato("        \n ---- OPCIONES ---- \n"
                   " A = Lista de Heroes  \n"
                   " B = Lista de Heroinas \n"
                   " C = Heroe mas alto\n"
                   " D = Heroina mas alta\n"
                   " E = Heroe mas bajo\n"
                   " F = Heroina mas baja\n"
                   " G = Promedio de altura masculino\n"
                   " H = Promedio de altura femenino\n"
                   " I = Cantidad color de ojos\n"
                   " J = Cantidad color de pelo\n"
                   " K = Cantidad nivel de inteligencia\n"
                   " L = Grupo de Heroes por color de ojos\n"
                   " M = Grupo de Heroes por color de pelo\n"
                   " N = Grupo de Heroes por tipo de inteligencia\n"
                   " Z = Salir del programa\n")

#imprimir_menu_desafio_5()      


#1.2
def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    opcion = input(" >")
    opcion = opcion[0]
    opcion = opcion.upper()
    validacion = re.search("[A-NZ]",opcion)
    if (validacion == None):
        retorno = -1
    else:
        retorno = opcion
    return retorno

#print(stark_menu_principal_desafio_5())

#1.3
def stark_marvel_app_5(lista_heroes:list):
    opcion = stark_menu_principal_desafio_5()
    
#stark_marvel_app_5(lista_personajes)

#1.4
def leer_archivo(nombre_archivo:str)->list:
    dic_json = {}
    with open(nombre_archivo,"r") as archivo:
        dic_json = json.load(archivo)
    return dic_json["heroes"]

#for personaje in lista_personajes:
#    print("\n")
#    print(personaje)
lista_personajes = leer_archivo("Clase_8\data_stark.json")

#1.5
def guardar_archivo(archivo_a_guardar:str,archivo_contenido:str):

    validacion = re.search("(.json|.csv)$",archivo_a_guardar)
    if (validacion == None):
        mensaje = f"Error al crear el archivo: {archivo_a_guardar}"
        retorno = False
    else:
        validacion = re.search("(.json)$",archivo_a_guardar)
        with open(archivo_a_guardar,"w+") as archivo:
            archivo_almacenado = archivo.write(archivo_contenido)
        if (validacion == None):
            mensaje = f"Se creó el archivo: {archivo_a_guardar}"
        else:
            mensaje = f"Se creó el archivo: {archivo_a_guardar}"
        print(mensaje)
        retorno = True
    return retorno

#guardar_archivo("Clase_8\data_nueva.json","Prueba")

#1.6
def capitalizar_palabras(dato:str):
    dato_nuevo = set(re.findall("[a-zA-Z]+",dato))
    for palabra in dato_nuevo:
        palabra_cap = palabra.capitalize()
        dato = re.sub(palabra,palabra_cap,dato)
    return dato

#print(capitalizar_palabras("233hola 233hola chau321"))

#1.7
def obtener_nombre_capitalizado(heroe:dict):
    nombre = capitalizar_palabras(heroe["nombre"])
    nombre_heroe = f"Nombre: {nombre}"
    return nombre_heroe
    
#print(obtener_nombre_capitalizado(lista_personajes[0]))

#1.8
def obtener_nombre_y_dato(heroe:dict,key:str) -> str:
    nombre = obtener_nombre_capitalizado(heroe)
    dato = heroe[key]
    key = key.capitalize()
    nombre_mas_dato = f"{nombre} | {key}: {dato} "
    return nombre_mas_dato

#print(obtener_nombre_y_dato(lista_personajes[0],"fuerza"))

#---------------------PUNTO 2----------------

#2.1
def es_genero(heroe:dict,genero:str) -> bool:
    retorno = False
    if (genero == heroe["genero"]):
        retorno = True
    return retorno

#print(es_genero(lista_personajes[0],"F"))

#2.2
def stark_guardar_heroe_genero(lista_heroes:list,genero:str):
    for heroe in lista_heroes:
        validacion = es_genero(heroe,genero)
        if (validacion == True):
            guardar_archivo("Clase_8\personajes.csv",heroe["nombre"])   
         


stark_guardar_heroe_genero(lista_personajes,"F")
#---------------------PUNTO 3----------------
#---------------------PUNTO 4----------------
#---------------------PUNTO 5----------------
#---------------------PUNTO 6----------------