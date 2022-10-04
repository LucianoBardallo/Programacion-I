import json
import re

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
    with open("PP_STARWARS\Archivo_exportado.csv","w") as archivo:
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

def ordenar_lista(lista_personajes:list,key:str,orden:str) -> list:
    '''
    Esta funcion se encarga de ordenar una lista

    Parametros: Recibe una lista de personajes de tipo list, una key que representa la clave por la que ordenar y un orden que determina para que lado

    Retorna: Una lista ordenada
    '''
    lista = lista_personajes.copy()
    lista_ordenada = []
    while(len(lista) > 0):
        max_min = buscar_max_min(lista,key,orden)
        lista_ordenada.append(lista.pop(max_min))
    return lista_ordenada

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

def calcular_genero_mas_alto(lista_personajes:list,key:str,orden:str) -> list:
    '''
    Esta funcion se encarga de calcular el personaje mas alte de cada genero

    Parametros: Una lista de personajes del tipo list, Una key que representa la altura, y un orden que representa la forma de la lista

    Retorna: Una lista con los personajes mas altos segun su genero
    '''
    lista_male = []
    lista_female = []
    lista_nogender = []
    for heroe in lista_personajes:
        if(heroe["gender"] == "male"):
            lista_male.append(heroe)
        elif(heroe["gender"] == "female"):
            lista_female.append(heroe)
        elif(heroe["gender"] == "n/a"):
            lista_nogender.append(heroe)

    lista_final = []
    for heroe in lista_female:
        max_min_f = buscar_max_min(lista_female,key,orden)
        heroina_mas_alta = lista_female[max_min_f]

    for heroe in lista_male:
        max_min_m = buscar_max_min(lista_male,key,orden)
        heroe_mas_alto = lista_male[max_min_m]
    
    for heroe in lista_nogender:
        max_min_ng = buscar_max_min(lista_nogender,key,orden)
        heroe_nogender = lista_nogender[max_min_ng]

    lista_final.append(heroina_mas_alta)
    lista_final.append(heroe_mas_alto)
    lista_final.append(heroe_nogender)

    return lista_final      
        
def buscar_heroe(lista_personajes:list) -> list:
    '''
    Esta funcion se encarga de buscar a cualquier heroe

    Parametros: Recibe una lista de personaje del tipo list

    Retorna: Una lista con los resultados de la busqueda
    '''
    lista_busqueda = []
    buscador = input("Ingrese el heroe a buscar: ")
    for heroe in lista_personajes:
        match = re.search(buscador,heroe["name"],re.IGNORECASE)
        if (match != None):
            lista_busqueda.append(heroe)
    return lista_busqueda
