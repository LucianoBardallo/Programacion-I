import json
import re

#------------------ Punto 0 -------------------

def leer_archivo(nombre_archivo:str) -> list:
    '''
    Esta funcion se encarga de cargar un archivo de solo lectura

    Parametros: La ruta del archivo que queremos cargar

    Retorna: Una lista con los heroes
    '''
    lista_archivo = {}
    with open(nombre_archivo,"r") as archivo:
        lista_archivo = json.load(archivo)
    return lista_archivo["heroes"]

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
    Esta funcion se encarga de obtener un dato del usuario y validarlo

    Retorna: El dato en caso de estar todo bien, -1 en caso contrario
    '''
    imprimir_menu()
    opcion = validar_dato_ingresado("Ingrese una opcion: ")
    return opcion

def validar_dato_ingresado(texto_usuario:str) -> str:
    '''
    Esta funcion se encarga de validar el dato ingresado en el menu principal

    Parametros: Un dato del tipo str que contiene lo que se le muestra al usuario

    Retorna: El dato ingresado, o -1 en caso contrario
    '''
    dato_ingresado = input(texto_usuario)
    dato_validado = re.match("^[1-7]{1}$",dato_ingresado)
    if (dato_validado == None):
        retorno = -1
    else:
        retorno = dato_ingresado
    return retorno

def convertir_lista_str_formateado(lista:list,key:str) -> str:
    '''
    Esta funcion se encarga de convertir una lista a un str

    Parametros: Una lista del tipo list, una key del tipo str

    Retorna: Toda la lista formateada en un str
    '''
    mensaje = ""
    for elemento in lista:
        mensaje += "{0} - {1}\n".format(elemento["nombre"],elemento[key])
    return mensaje

def dividir(dividendo:int,divisor:int) -> int:
    '''
    Esta funcion se encarga de dividir

    Parametros: Recibe un numero que representa el dividendo y otro que representa el divisor

    Retorna: El resultado de la division o un - 0 - en caso de no poder hacerse
    '''
    if (divisor == 0):
        retorno = 0
    else:
        division = dividendo // divisor
        retorno = division
    return retorno

def validar_respuesta(respuesta:str,patron:str):
    '''
    Esta funcion se encarga de validar datos en general

    Parametros: Una respuesta del tipo str que es el dato a validar, Un patron del tipo str que es la expresion regular

    Retorna: El dato validado o -1 en caso contrario
    '''
    retorno = -1
    if respuesta:
        if(re.match(patron,respuesta)):
            retorno = respuesta
    return retorno


#------------------ Punto 1 -------------------

def mostrar_heroes(lista_heroes:list,cantidad:int) -> list:
    '''
    Esta funcion se encarga de mostrar la lista de heroes hasta la cantidad que nosotros queramos

    Parametros: Una lista de heroes del tipo str, una cantidad que va a ser nuestro maximo

    Retorna: Una lista cortada hasta el punto que le hayamos indicado
    '''
    lista = lista_heroes[:]
    lista = lista[:cantidad]
    return lista

#------------------ Punto 2 -------------------
#------------------ Punto 3 -------------------
def buscar_max_minimo(lista:list,key:str,order:str) -> int:
    '''
    Esta funcion se encarga de encontrar la posicion minima o maxima de una lista

    Parametros: Una lista de heroes del tipo list, una key del tipo str que representa la clave a buscar, y un orden que determina el ordenamiento de la lista

    Retorna: La posicion del elemento a buscar o -1 en caso contrario
    '''
    retorno = -1
    if (len(lista) > 0):
        min_max = 0
        for i in range(len(lista)):
            if ((order == "asc" and lista[min_max][key] > lista[i][key]) or (order == "desc" and lista[min_max][key] < lista[i][key])):
                min_max = i
        retorno = min_max
    return retorno       

def ordenar_dato(lista:list,key:str,order:str) -> list:
    '''
    Esta funcion se encarga de ordenar una lista

    Parametros: Una lista de heroes del tipo list, una key que representa la clave a ordenar, y el orden que determminar el ordenamiento de la lista

    Retorna: Una lista ordenada por la clave ingresada y el orden dado
    '''
    lista_copiada = lista[:]
    lista_ordenada = []
    while(len(lista_copiada) > 0):
        max_min = buscar_max_minimo(lista_copiada,key,order)
        lista_ordenada.append(lista_copiada.pop(max_min))
    return lista_ordenada   

#------------------ Punto 4 -------------------
def sumar_dato(lista_heroes:list,key:str) -> str:
    '''
    Esta funcion se encarga de sumar datos numericos y agregarlo en una nueva variable

    Parametros: Una lista de heroes del tipo list, y una key del tipo str que representa la clave a ser evaluada

    Retona: La suma obtenida
    '''
    sumar = 0
    for heroe in lista_heroes:
        sumar += heroe[key]
    return sumar

def cantidad_heroes(lista_heroes:list) -> int:
    '''
    Esta funcion se encarga de contar la cantidad de heroes de la lista

    Parametros: Una lista de heroes del tipo str

    Retona: La cantidad de heroes
    '''
    cantidad = 0
    for heroe in lista_heroes:
        cantidad += 1
    return cantidad

def calcular_promedio(lista_heroes:list,key:str) -> int:
    '''
    Esta funcion se encarga de calcular el promedio de un dato en especifico

    Parametros: Una lista de heroes del tipo list, una key del tipo str que representa la clave a ser evaluada

    Retona: El promedio obtenido
    '''
    suma = sumar_dato(lista_heroes,key)
    cantidad = cantidad_heroes(lista_heroes)
    retorno = dividir(suma,cantidad)
    return retorno

def filtrar_por_dato(lista_heroes:list,key:str,tipo:str) -> list:
    '''
    Esta funcion se encarga de filtrar los datos que esten por debajo o arriba del promedio

    Parametros: Una lista de heroes del tipo list, una key del tipo str que representa la clave a ser evaluada 
    y un tipo que puede tomar el valor de menor para mostrar los que estan debajo del promedio y mayor en caso de querer mostrar solo los que esten por arriba

    Retorna: Una lista que muestre datos debajo del promedio o arriba del mismo
    '''
    promedio = calcular_promedio(lista_heroes,key)
    print(f"Promedio - {promedio}")
    tipo = tipo.lower()
    lista_promedio = []
    for heroe in lista_heroes:
        if(tipo == "mayor" and promedio < heroe[key]):
            lista_promedio.append(heroe)
            order = "asc"
        elif(tipo == "menor" and promedio > heroe[key]):
            lista_promedio.append(heroe)
            order = "desc"
    lista_promedio = ordenar_dato(lista_promedio,key,order)
    return lista_promedio

#------------------ Punto 5 -------------------
def buscar_heroe_tipo(lista_heroes:list,key:str,tipo:str) -> list:
    '''
    Esta funcion se encarga de buscar un heroe por alguna clave en especifico

    Parametros: Una lista de heroes del tipo list, una key del tipo str que representa la clave a evaluar y tipo que es el valor de la clave que queremos buscar

    Retorna: Una lista que contiene los heroes que coincidieron con la busqueda
    '''
    lista_inteligencia = []
    for heroe in lista_heroes:
        if (heroe[key] == tipo):
            lista_inteligencia.append(heroe)
    return lista_inteligencia

#------------------ Punto 6 -------------------
def exportar_csv(mensaje:str):
    '''
    Esta funcion se encarga de exportar un dato a un archivo .csv

    Parametros: Un mensaje del tipo str que contiene los datos a ingresar al archivo
    '''
    with open("Clase_10\Ejercicio12\lista_exportada.csv","w") as archivo:
        mensaje = archivo.write(mensaje)

