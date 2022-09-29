import json
import re

#VALIDACIONES
def validar_dato_menu(texto_usuario:str) -> str:
    '''
    Esta funcion se encarga de obtener y validar un dato ingresado por el usuario

    Parametros: Un dato del tipo str que contiene lo que ingresa el usuario

    Retorna: El dato ingresado, o -1 en caso contrario
    '''
    retorno = -1
    dato_ingresado = input(texto_usuario)
    dato_validado = re.match("^[1-7]{1}$",dato_ingresado)
    if (dato_validado != None):
        retorno = dato_ingresado
    return retorno

def validar_respuesta_general(respuesta:str,patron:str) -> str:
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
    opcion = validar_dato_menu("Ingrese una opcion: ")
    return opcion

def importar_archivo(path:str) -> list:
    '''
    Esta funcion se encarga de importar el archivo que le pasemos por parametro a una lista nueva

    Parametros: Una direccion del tipo str que va a ser la ruta de donde exportemos

    Retorna: Una lista con los datos importados
    '''
    with open(path,"r") as archivo:
        lista = json.load(archivo)
    return lista["heroes"]

#PUNTOS
def mostrar_heroe_formateado(lista_heroes:list) -> str:
    mensaje = ""
    for heroe in lista_heroes:
        mensaje += "\nNombre: {0}\nIdentidad: {1}\nAltura: {2}\nPeso: {3}\nFuerza {4}\nInteligencia: {5}\n".format(heroe["nombre"],heroe["identidad"],heroe["altura"],heroe["peso"],heroe["fuerza"],heroe["inteligencia"])
    return mensaje

def convertir_lista_a_str():
    pass

def mostrar_heroes(lista_hereos:list,cantidad:int) -> list:
    '''
    Esta funcion mostrara los heroes dependiendo de la cantidad seleccionada por el usuario
    
    Parametro: Una lista de heroes del tipo list, un dato cantidad del tipo int que representa hasta donde leer la lista

    Retorna: Una lista cortada por la cantidad ingresada
    '''
    lista = lista_hereos[:]
    lista_cortada = lista[:cantidad]
    return lista_cortada

def buscar_min_max(lista_heroes:list,key:str,orden:str) -> int:
    '''
    Esta funcion se encarga de buscar la posicion de la lista con el valor maximo o minimo

    Parametros: Una lista de heroes del tipo list, Una key que representa la clave a evaluar 
    y un orden que decide si devuelve la posicion maxima o minima

    Retorna: Posicion minima o maxima del dato evaluado
    '''
    retorno = -1
    if (len(lista_heroes) > 0):
        min_max = 0
        for i in range(len(lista_heroes)):
            if (orden == "asc" and lista_heroes[min_max][key] > lista_heroes[i][key] or orden == "desc" and lista_heroes[min_max][key] < lista_heroes[i][key]):
                min_max = i
        retorno = min_max
    return retorno

def ordenar_lista(lista_heroes:list,key:str,orden:str) -> list:
    '''
    Esta funcion se encarga de ordenar una lista

    Parametros: Una lista de heroes del tipo list, una key que representa la clave a ordenar, y el orden que determminar el ordenamiento de la lista

    Retorna: Una lista ordenada por la clave ingresada y el orden dado
    '''
    lista = lista_heroes[:]
    lista_ordenada = []
    while(len(lista) > 0):
        min_max = buscar_min_max(lista,key,orden)
        lista_ordenada.append(lista.pop(min_max))
    return lista_ordenada

def sumar_dato(lista_heroes:list,key:str):
    '''
    Esta funcion se encarga de sumar datos numericos y agregarlo en una nueva variable

    Parametros: Una lista de heroes del tipo list, y una key del tipo str que representa la clave a ser evaluada

    Retona: La suma obtenida
    '''
    suma = 0
    for heroe in lista_heroes:
        suma += heroe[key]
    return suma

def calcular_cantidad_heroe(lista_heroes:list) -> int:
    '''
    Esta funcion se encarga de contar la cantidad de heroes de la lista

    Parametros: Una lista de heroes del tipo str

    Retona: La cantidad de heroes
    '''
    cantidad = 0
    for elemento in lista_heroes:
        cantidad += 1
    return cantidad

def dividir(dividendo:int,divisor:int) -> int:
    '''
    Esta funcion se encarga de dividir

    Parametros: Recibe un numero que representa el dividendo y otro que representa el divisor

    Retorna: El resultado de la division o un - 0 - en caso de no poder hacerse
    '''
    if (divisor == 0):
        retorno = -1
    else:
        division = dividendo // divisor
        retorno = division
    return retorno

def calcular_promedio(lista_heroes:list,key:str) -> int:
    '''
    Esta funcion se encarga de calcular el promedio de un dato en especifico

    Parametros: Una lista de heroes del tipo list, una key del tipo str que representa la clave a ser evaluada

    Retona: El promedio obtenido
    '''
    suma = sumar_dato(lista_heroes,key)
    cantidad = calcular_cantidad_heroe(lista_heroes)
    promedio = suma // cantidad
    return promedio

def filtrar_heroes_por_dato(lista_heroes:list,key:str,tipo:str):
    '''
    Esta funcion se encarga de filtrar los datos que esten por debajo o arriba del promedio

    Parametros: Una lista de heroes del tipo list, una key del tipo str que representa la clave a ser evaluada 
    y un tipo que puede tomar el valor de menor para mostrar los que estan debajo del promedio y mayor en caso de querer mostrar solo los que esten por arriba

    Retorna: Una lista que muestre datos debajo del promedio o arriba del mismo
    '''
    promedio = calcular_promedio(lista_heroes,key)
    print(f"\nPromedio - {promedio}")
    lista_ordenada = []
    for heroe in lista_heroes:
        if (tipo == "menor" and promedio < heroe[key]):
            lista_ordenada.append(heroe)
            orden = "asc"
        elif (tipo == "mayor" and promedio > heroe[key]):
            lista_ordenada.append(heroe)
            orden = "desc"
    lista_ordenada = ordenar_lista(lista_ordenada,key,orden)
    return lista_ordenada

def buscar_e_imprimir_heroe_tipo(lista_heroes:list,key:str,tipo:str):
    '''
    Esta funcion se encarga de buscar un heroe por alguna clave en especifico e imprimirlo por pantalla

    Parametros: Una lista de heroes del tipo list, una key del tipo str que representa la clave a evaluar y tipo que es el valor de la clave que queremos buscar
    '''
    for heroe in lista_heroes:
        if(heroe["inteligencia"] == ""):
            heroe["inteligencia"] = "No tiene"
        match = re.search(tipo,heroe[key])
        if(match != None):
            mensaje = "\nNombre: {0}\nIdentidad: {1}\nAltura: {2}\nPeso: {3}\nFuerza {4}\nInteligencia: {5}".format(heroe["nombre"],heroe["identidad"],heroe["altura"],heroe["peso"],heroe["fuerza"],heroe["inteligencia"])
            print(mensaje)

def exportar_csv(mensaje:str):
    '''
    Esta funcion se encarga de exportar un dato a un archivo .csv

    Parametros: Un mensaje del tipo str que contiene los datos a ingresar al archivo
    '''
    with open("Clase_10\Ejercicio12\lista_exportada.csv","w") as archivo:
        mensaje = archivo.write(mensaje)
        print("El archivo se creo con exito")

