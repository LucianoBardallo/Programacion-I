import json
import re

#VALIDACIONES
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
    print("\n\tOpciones"
    "\n\t1 - Mostrar pokemones"
    "\n\t2 - Mostrar pokemones por poder"
    "\n\t3 - Mostrar pokemones por id"
    "\n\t4 - Calcular promedio"
    "\n\t5 - Buscar pokemon tipo"
    "\n\t6 - Exportar archivo"
    "\n\t7 - Salir\n")

def obtener_opcion_principal(mensaje:str) -> str:
    opcion = validar_dato_general(mensaje,"^[1-7]+")
    return opcion

#MAIN
def importar_archivo(path:str) -> list:
    with open(path,"r") as archivo:
        lista = json.load(archivo)
    return lista["pokemones"]

def mostrar_pokemones(lista_pokemones:list,cantidad:int) -> list:
    lista = lista_pokemones[:]
    lista_cortada = lista[:cantidad]
    return lista_cortada

def buscar_maximo_minimo(lista_pokemones:list,key:str,orden:str) -> int:
    max_min = 0
    for i in range(len(lista_pokemones)):
        if ((orden == "desc" and lista_pokemones[i][key] > lista_pokemones[max_min][key]) or (orden == "asc" and lista_pokemones[i][key] < lista_pokemones[max_min][key])):
            max_min = i
    return max_min

def ordenar_lista(lista_pokemones:list,key:str,orden:str):
    lista = lista_pokemones[:]
    lista_ordenada = []
    while (len(lista) > 0):
        max_min = buscar_maximo_minimo(lista,key,orden)
        lista_ordenada.append(lista.pop(max_min))
    return lista_ordenada

def formatear_lista(lista_pokemones:list) -> str:
    mensaje = ""
    for pokemon in lista_pokemones:
        sacar_tipo = "-".join(pokemon["tipo"])
        sacar_evoluciones = "-".join(pokemon["evoluciones"])
        sacar_fortaleza = "-".join(pokemon["fortaleza"])
        sacar_debilidad = "-".join(pokemon["debilidad"])
        mensaje += "ID: {0} | {1} | Tipo: {2} | Evoluciones: {3} | Poder: {4} | Fortaleza: {5} | Debilidad: {6}\n".format(pokemon["id"],pokemon["nombre"],sacar_tipo,sacar_evoluciones,pokemon["poder"],sacar_fortaleza,sacar_debilidad)
    return mensaje

def sumar_dato(lista_pokemones:list,key:str):
    suma = 0
    for pokemon in lista_pokemones:
        suma += len(pokemon[key])
    return suma

def calcular_promedio(lista_pokemones:list,key:str):
    suma = sumar_dato(lista_pokemones,key)
    cantidad = len(lista_pokemones)
    promedio = suma // cantidad
    return promedio

def filtrar_lista_por_promedio(lista_pokemones:list,key:str,tipo:str) -> list:
    promedio = calcular_promedio(lista_pokemones,key)
    print("Promedio: {0}".format(promedio))
    lista_filtrada = []
    orden = "desc"
    for pokemon in lista_pokemones:
        if (tipo == "mayor" and len(pokemon[key]) > promedio):
            orden = "desc"
            lista_filtrada.append(pokemon)
        elif (tipo == "menor" and len(pokemon[key]) < promedio):
            orden = "asc"
            lista_filtrada.append(pokemon)
    lista_ordenada = ordenar_lista(lista_filtrada,key,orden)
    return lista_ordenada

def buscar_heroe_por_tipo(lista_pokemones:list,tipo:str):
    lista_busqueda = []
    for pokemon in lista_pokemones:
        for elemento in pokemon["tipo"]:
            match = re.search(tipo,elemento,re.IGNORECASE)
            if match != None:
                lista_busqueda.append(pokemon)
    return lista_busqueda

def exportar_archivo(lista_pokemones:list):
    with open("Practica\Parcial_2\Archivo_exportado.csv","w") as archivo:
        archivo.write(lista_pokemones)
        print("El archivo se exporto exitosamente")