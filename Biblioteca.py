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

def validar_respuesta_int(respuesta:str):
    '''
    Esta funcion se encarga de validar el dato ingresado por el usuario para que sea un int

    Parametros: Un dato del tipo str que contiene lo que ingresa el usuario

    Retorna: El dato ingresado, o -1 en caso contrario
    '''
    retorno = -1
    if respuesta:
        if(re.match("[0-9]+",respuesta)):
            retorno = respuesta
    return retorno

def validar_respuesta_str(respuesta:str):
    '''
    Esta funcion se encarga de validar el dato ingresado por el usuario para que sea un str

    Parametros: Un dato del tipo str que contiene lo que ingresa el usuario

    Retorna: El dato ingresado, o -1 en caso contrario
    '''
    retorno = -1
    if respuesta:
        if(re.match("[a-zA-Z]+",respuesta)):
            respuesta.upper()
            retorno = respuesta
    return retorno

def validar_respuesta_tipo(respuesta:str):
    '''
    Esta funcion se encarga de validar el dato ingresado por el usuario para que sea un valor determinado

    Parametros: Un dato del tipo str que contiene lo que ingresa el usuario

    Retorna: El dato ingresado, o -1 en caso contrario
    '''
    retorno = -1
    if respuesta:
        if(re.match("^good|average|high$",respuesta)):
            respuesta.upper()
            retorno = respuesta
    return retorno

def validar_respuesta_error(lista_heroes:list,respuesta:str,mensaje:str):
    if respuesta == -1:
        retorno = mensaje
    else:
        retorno = lista_heroes
    return retorno
        