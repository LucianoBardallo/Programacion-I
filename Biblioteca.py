import re

def validar_respuesta(respuesta:str,patron:str):
    retorno = -1
    if respuesta:
        if(re.match(patron,respuesta)):
            retorno = respuesta
    return retorno

def validar_respuesta(respuesta:str):
    retorno = -1
    if respuesta:
        if(re.match("[0-9]+",respuesta)):
            retorno = respuesta
    return retorno

def validar_respuesta(respuesta:str):
    retorno = -1
    if respuesta:
        if(re.match("[a-zA-Z]+",respuesta)):
            respuesta.upper()
            retorno = respuesta
    return retorno

def validar_respuesta(respuesta:str):
    retorno = -1
    if respuesta:
        if(re.match("^good|average|high$",respuesta)):
            respuesta.upper()
            retorno = respuesta
    return retorno