import re

def validar_dato(texto_usuario:str,patron:str) -> str:
    '''
    Esta funcion se encarga de obtener y validar un dato ingresado por el usuario

    Parametros: Un dato del tipo str que contiene lo que ingresa el usuario, 
    y un dato del tipo str que contiene el patron que vamos a usar para validar

    Retorna: El dato ingresado, o -1 en caso contrario
    '''
    retorno = -1
    dato_ingresado = input(texto_usuario)
    dato_validado = re.match(patron,dato_ingresado)
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