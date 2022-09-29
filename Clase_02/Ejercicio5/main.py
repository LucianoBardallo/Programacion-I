habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    }
]

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

lista_ordenada = ordenar_dato(habilidades,"Poder","desc")

for elemento in lista_ordenada:
    print("{0} - Poder: {1}".format(elemento["Nombre"],elemento["Poder"]))


