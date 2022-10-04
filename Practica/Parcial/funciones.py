import json
import re

def validar_dato_menu(texto_usuario:str) -> str:
    '''
    Esta funcion se encarga de obtener y validar un dato ingresado por el usuario

    Parametros: Un dato del tipo str que contiene lo que ingresa el usuario

    Retorna: El dato ingresado, o -1 en caso contrario
    '''
    retorno = -1
    dato_ingresado = input(texto_usuario)
    dato_ingresado = dato_ingresado.lower()
    dato_validado = re.match("^[1-7]{1}$",dato_ingresado)
    if (dato_validado != None):
        retorno = dato_ingresado
    return retorno

def validar_dato_general(texto_usuario:str,patron:str) -> str:
    '''
    Esta funcion se encarga de obtener y validar un dato ingresado por el usuario

    Parametros: Un dato del tipo str que contiene lo que ingresa el usuario

    Retorna: El dato ingresado, o -1 en caso contrario
    '''
    dato_ingresado = input(texto_usuario)
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
     
def normalizar_datos(lista_pokemones:list):
    lista = lista_pokemones[:]
    cambio = False
    for pokemon in lista:
        for clave in pokemon:
            if (len(lista) > 0):
                if (type(pokemon[clave]) == type("")):
                    if (re.match("[a-zA-Z]+",pokemon[clave])):
                        pokemon[clave] = pokemon[clave].capitalize()
                    elif (re.match("[0-9]+",pokemon[clave])):
                        pokemon[clave] = int(pokemon[clave])
                    elif (re.match("[0-9.,]+",pokemon[clave])):
                        pokemon[clave] = float(pokemon[clave])
            else:
                print("\nError: Lista de heroes vacia")   
    if (cambio == True):
        print("\n---Datos normalizados---\n")
    return lista 

def importar_archivo(path:str) -> list:
    '''
    Esta funcion se encarga de importar un archivo json

    Parametros: Una dato str que representa la ruta de donde vamos a importar el archivo

    Retorna: Una lista de pokemones
    '''
    with open(path,"r") as archivo:
        lista = json.load(archivo)
    return lista["pokemones"]

def imprimir_menu():
    '''
    Esta funcion se encarga de imprimir el menu
    '''
    print("\n\tOPCIONES\n"
        "1- Mostrar pokemones\n"
        "2- Ordenar lista pokemones por poder\n"
        "3- Ordenar lista pokemones por ID\n"
        "4- Calcular promedio\n"
        "5- Buscar heroes por tipo\n"
        "6- Exportar archivo\n"
        "7- Salir\n")

def menu_principal():
    '''
    Esta funcion se encarga de imprimir el menu y tomar la opcion ingresada por el usuario
    '''
    imprimir_menu()
    opcion = validar_dato_menu("Ingrese una opcion: ")
    return opcion

def mostrar_pokemones(lista_pokemones:list,cantidad:int) -> list:
    '''
    Esta funcion se encarga de mostrar una lista de pokemones cortada por la cantidad ingresada del usuario

    Parametros: Una lista de pokemones del tipo list, Un dato tipo int que representa la cantidad a cortar la lista

    Retorna: Una lista cortada
    '''
    lista = lista_pokemones[:]
    lista_cortada = lista[:cantidad]
    return lista_cortada

def buscar_max_min(lista_pokemones:list,key:str,orden:str) -> int:
    '''
    Esta funcion se encarga de buscar el dato minimo o maximo de una lista

    Parametros: Una lista de pokemones del tipo list, Una clave que representa el dato a buscar, y el orden que determina si es maximo o minimo

    Retonar: Un entero que representa la posicion minima o maxima
    '''
    max_min = 0
    for i in range(len(lista_pokemones)):
        if ((orden == "desc" and lista_pokemones[max_min][key] < lista_pokemones[i][key]) or (orden == "asc" and lista_pokemones[max_min][key] > lista_pokemones[i][key])):
            max_min = i
    return max_min

def ordenar_lista(lista_pokemones:list,key:str,orden:str) -> list:
    '''
    Esta funcion se encarga de ordenar una lista por el dato y el orden ingresado

    Parametros: Una lista de pokemones del tipo list, una clave que representa el dato a ordenar y un orden que determina el orden de la lista

    Rertonar: Una lista ordenada
    '''
    lista = lista_pokemones[:]
    lista_ordenada = []
    while(len(lista) > 0):
        max_min = buscar_max_min(lista,key,orden)
        lista_ordenada.append(lista.pop(max_min))
    return lista_ordenada

def formatear_lista(lista:list):
    mensaje = ""
    for heroe in lista:
        mensaje += "\nID: {0}\nNombre: {1}\nTipo: {2}\nEvoluciones: {3}\nPoder: {4}\nFortaleza: {5}\nDebilidad: {6},\n".format(heroe["id"],heroe["nombre"],heroe["tipo"],heroe["evoluciones"],heroe["poder"],heroe["fortaleza"],heroe["debilidad"])
    return mensaje

def sumar_dato(lista_pokemones:list,key:str) -> int:
    suma = 0 
    for pokemon in lista_pokemones:
        for i in range(len(pokemon[key])):
            suma += 1
    return suma

def cantidad_pokemones(lista_pokemones:list):
    cantidad = 0
    for pokemon in lista_pokemones:
        cantidad += 1
    return cantidad

def dividir(dividendo:int,divisor:int) -> int:
    if (divisor == 0):
        retorno = 0
    else:
        retorno = dividendo // divisor
    return retorno

def calcular_promedio(lista_pokemones:list,key:str):
    suma = sumar_dato(lista_pokemones,key)
    cantidad = cantidad_pokemones(lista_pokemones)
    promedio = dividir(suma,cantidad)
    return promedio

def filtrar_pokemon_por_promedio(lista_pokemones:list,key:str,tipo:str):
    promedio = calcular_promedio(lista_pokemones,key)
    print(f"Promedio: {promedio}")
    lista_filtro = []
    orden = "asc"
    for pokemon in lista_pokemones:
        if (tipo == "menor" and len(pokemon[key]) < promedio):
            orden = "desc"
            lista_filtro.append(pokemon)
        elif(tipo == "mayor" and len(pokemon[key]) > promedio):
            orden = "asc"
            lista_filtro.append(pokemon)
    lista_ordenada = ordenar_lista(lista_filtro,key,orden)
    return lista_ordenada

def buscar_pokemon_dato(lista_pokemones:list,key:str,tipo:str):
    lista_filtrada = []
    for heroe in lista_pokemones:
        for i in range(len(heroe[key])):
            match = re.search(tipo,heroe[key][i])
            if match != None:
                lista_filtrada.append(heroe)
    return lista_filtrada

def exportar_archivo(contenido:str):
    with open("Practica\Parcial\Archivo_exportado.csv","w") as archivo:
        archivo.write(contenido)
        print("El archivo se creo con exito")
