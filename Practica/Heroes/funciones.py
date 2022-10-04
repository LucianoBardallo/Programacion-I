import json
import re

def validar_dato_general(texto_usuario:str,patron:str) -> str:
    '''
    Esta funcion se encarga de obtener y validar un dato ingresado por el usuario

    Parametros: Un dato del tipo str que contiene lo que ingresa el usuario

    Retorna: El dato ingresado, o -1 en caso contrario
    '''
    dato_ingresado = input(texto_usuario)
    dato_ingresado = dato_ingresado.lower()
    dato_ingresado = validar_respuesta(dato_ingresado,patron)
    return dato_ingresado

def validar_respuesta(respuesta:str,patron:str) -> str:
    '''
    Esta funcion se encarga de validar el dato ingresado por el usuario

    Parametros: Un dato del tipo str que contiene lo que ingresa el usuario, 
    y un dato del tipo str que contiene el patron que vamos a usar para validar

    Retorna: El dato ingresado, o -1 en caso contrario
    '''
    retorno = -1
    if respuesta:
        if(re.match(patron,respuesta)):
            retorno = respuesta
    return retorno


#MENU
def imprimir_menu():
    '''
    Esta funcion se encarga de imprimir el menu
    '''
    print('''\n\tOPCIONES
     1 - Mostrar lista de heroes
     2 - Mostrar lista de heroes por altura
     3 - Mostrar lista de heroes por fuerza
     4 - Calcular promedio
     5 - Buscar heroes por inteligencia
     6 - Exportar
     7 - Salir
    ''')

def menu_principal():
    '''
    Esta funcion se encarga de imprimir el menu principal e tomar la opcion ingresada por el usuario

    Retona: La opcion dada por el usuario
    '''
    imprimir_menu()
    opcion = validar_dato_general("Ingrese una opcion: ","^[1-7]{1}$")
    return opcion

def importar_archivo(path:str) -> list:
    with open(path,"r") as archivo:
        lista = json.load(archivo)
    return lista["heroes"]

def mostrar_heroes(lista_heroes:list,cantidad:int) -> list:
    lista = lista_heroes[:]
    lista_cortada = lista[:cantidad]
    return lista_cortada

def buscar_max_min(lista_heroes:list,key:str,orden:str):
    max_min = 0
    for i in range(len(lista_heroes)):
        if((orden == "asc" and lista_heroes[i][key] < lista_heroes[max_min][key]) or (orden == "desc" and lista_heroes[i][key] > lista_heroes[max_min][key])):
            max_min = i
    return max_min

def ordenar_lista(lista_heroes:list,key:str,orden:str):
    lista = lista_heroes[:]
    lista_ordenada = []
    while(len(lista) > 0):
        max_min = buscar_max_min(lista,key,orden)
        lista_ordenada.append(lista.pop(max_min))
    return lista_ordenada

def sumar_dato(lista_heroes:list,key:str):
    suma = 0
    for heroe in lista_heroes:
        suma += heroe[key]
    return suma

def calcular_promedio(lista_heroes:list,key:str):
    suma = sumar_dato(lista_heroes,key)
    cantidad = len(lista_heroes)
    promedio = suma // cantidad
    return promedio

def filtrar_heroe_por_promedio(lista_heroes:list,key:str,tipo:str):
    promedio = calcular_promedio(lista_heroes,key)
    print("Promedio: {0}".format(promedio))
    lista_filtrada = []
    for heroe in lista_heroes:
        if((tipo == "menor" and promedio > heroe[key]) or (tipo == "mayor" and promedio < heroe[key])):
            lista_filtrada.append(heroe)
    return lista_filtrada

