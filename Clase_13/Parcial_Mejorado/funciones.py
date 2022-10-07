import json
import re
from functools import reduce

def cargar_json(path:str) -> list:
    '''
    Esta funcion se encarga de leer el archivo y guardarlo en una variable.

    Parametros: Recibe un path que es la ruta de donde se obtiene el archivo

    Retorna: Una lista
    '''
    with open(path,"r") as archivo:
        lista = json.load(archivo)
    return lista["results"]

def exportar_archivo(mensaje:str):
    '''
    Esta funcion se encarga de exportar el contenido de una variable a un archivo

    Parametros: Un mensaje tipo string que funciona como el contenido a exportar
    '''
    with open("Parcial_Mejorado\Archivo_exportado.csv","w") as archivo:
        mensaje = archivo.write(mensaje)
        print("El archivo se creo exitosamente")

def buscar_max_min(lista_personajes:list,key:str,orden:str) -> int:
    '''
    Esta funcion se encarga de encontrar el elemento minimo de una lista
    '''
    max_min = 0
    for i in range(len(lista_personajes)):
        if((orden == "desc" and lista_personajes[i][key] > lista_personajes[max_min][key]) or (orden == "asc" and lista_personajes[i][key] < lista_personajes[max_min][key])):
            max_min = i
    return max_min
    
def normalizar_datos(lista_personjes:list) -> list:
    '''
    Esta funcion se encarga de normalizar los datos segun corresponda

    Parametros: Recibe una lista de personajes del tipo list

    Retorna: Retorna una lista normalizada
    '''
    lista_normalizada = []
    for heroe in lista_personjes:
        dic_heroe = {}
        dic_heroe["name"] = heroe["name"]
        dic_heroe["height"] = int(heroe["height"])
        dic_heroe["mass"] = int(heroe["mass"])
        dic_heroe["gender"] = heroe["gender"]
        lista_normalizada.append(dic_heroe)
    return lista_normalizada

def formatear_mensaje(lista_personaje:list) -> str:
    '''
    Esta funcion se encarga de formatear una lista de forma que quede un mensaje del tipo str

    Paramtros: Recibe una lista del tipo list
    '''
    mensaje = ""
    for heroe in lista_personaje:
        mensaje += "{0},{1},{2},{3}\n".format(heroe["name"],heroe["height"],heroe["mass"],heroe["gender"])
    return mensaje

def mostrar_heroes(lista_personajes:list):
    '''
    Esta funcion se encarga de mostrar de mejor forma la lista

    Paramtros: Recibe una lista del tipo list
    '''
    for heroe in lista_personajes:
        print("\nNombre: {0}\nAltura: {1}\nPeso: {2}\nGenero: {3}".format(heroe["name"],heroe["height"],heroe["mass"],heroe["gender"]))

def calcular_genero_mas_alto(lista_personajes:list,key:str) -> list:
    '''
    Esta funcion se encarga de calcular el personaje mas alte de cada genero

    Parametros: Una lista de personajes del tipo list, Una key que representa la altura, y un orden que representa la forma de la lista

    Retorna: Una lista con los personajes mas altos segun su genero
    '''
    lista_personajes.sort(key = lambda personaje: personaje[key], reverse = True)
    lista_male = list(filter(lambda elem : elem["gender"] == "male" ,lista_personajes))
    lista_female = list(filter(lambda elem : elem["gender"] == "female",lista_personajes))
    lista_nogender = list(filter(lambda elem : elem["gender"] == "n/a",lista_personajes))
    lista_final = []
    lista_final.append(lista_male[0])
    lista_final.append(lista_female[0])
    lista_final.append(lista_nogender[0])

    return lista_final
  
        
def buscar_heroe(lista_personajes:list) -> list:
    '''
    Esta funcion se encarga de buscar a cualquier heroe

    Parametros: Recibe una lista de personaje del tipo list

    Retorna: Una lista con los resultados de la busqueda
    '''
    lista_busqueda = []
    buscador = input("Ingrese el heroe a buscar: ")
    lista_busqueda = list(map(lambda heroe: heroe if re.search(buscador,heroe["name"],re.IGNORECASE) != None else "",lista_personajes))
    lista_busqueda = list(filter(lambda elem : elem != "", lista_busqueda))
    return lista_busqueda
