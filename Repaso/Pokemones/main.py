from data_pokemone import pokemones

'''
{
            "id": 1,
            "nombre": "bulbasaur",
            "tipo": ["planta"],
            "evoluciones": ["ivysaur", "venusaur"],
            "poder": 4,
            "fortaleza":["agua"],
            "debilidad":["fuego"]
        },
        {
            "id": 4,
            "nombre": "charmander",
            "tipo": ["fuego"],
            "evoluciones": ["charmeleon", "charizard"],
            "poder": 5,
            "fortaleza":["planta"],
            "debilidad":["agua"]
        },
'''

#---------------------PUNTO 1----------------

#1.1
def obtener_nombre_pokemon(pokemon:dict) -> str:
    '''
    Esta funcion se encarga de obtener el nombre del pokemon

    Parametros: Un diccionario representando al pokemon

    Retorna: String con el nombre del pokemon
    '''
    nombre_pokemon = pokemon["nombre"]
    return nombre_pokemon

#print(obtener_nombre_pokemon(pokemones[1]))   

#1.2
def pokedex_imprimir_pokemones(pokemones:list):
    '''
    Esta funcion se encarga de imprimir la lista de nombre de los pokemones

    Parametros: Una lista representando a los pokemones
    '''
    for pokemon in pokemones:
        nombre_pokemon = obtener_nombre_pokemon(pokemon)
        print(nombre_pokemon)

#pokedex_imprimir_pokemones(pokemones)     

#---------------------PUNTO 2----------------

#2.1
def tiene_id_par(pokemon:dict) -> bool:
    '''
    Esta funcion se encarga de analizar si la ID del pokemon es par o impar

    Parametros: Un diccionario representando al pokemon

    Retorna: True si es par, False en caso contrario
    '''
    retorno = False
    if(pokemon["id"] % 2 == 0):
        retorno = True

    return retorno

#tiene_id_par(pokemones[1])

#2.2
def obtener_id_pokemon(pokemon:dict) -> str:
    '''
    Esta funcion se encarga de obtener el ID del pokemon

    Parametros: Un diccionario representando al pokemon

    Retorna: El ID del pokemon en forma de String
    '''
    id_pokemon = str(pokemon["id"])
    return id_pokemon

#print(obtener_id_pokemon(pokemones[1]))

#2.3
def pokedex_imprimir_pokemones_id_par(pokemones:list):
    '''
    Esta funcion se encarga de imprimir los pokemones si su ID es par

    Parametros: Un diccionario representando al pokemon
    '''
    for pokemon in pokemones:
        nombre_pokemon = obtener_nombre_pokemon(pokemon)
        id_pokemon = obtener_id_pokemon(pokemon)
        id_par = tiene_id_par(pokemon)
        if (id_par == True):
            print(f"Nombre: {nombre_pokemon} - ID: {id_pokemon}")

#pokedex_imprimir_pokemones_id_par(pokemones)

#---------------------PUNTO 3----------------

#3.1
def id_multiplo_25(pokemon:dict) -> bool:
    '''
    Esta funcion se encarga de analizar si la ID del pokemon es multiplo de 25

    Parametros: Un diccionario representando al pokemon

    Retorna: True si el ID es multiplo de 25, False en caso contrario
    '''
    retorno = False
    if (pokemon["id"] % 25 == 0):
        retorno = True
    return retorno

#for pokemon in pokemones:
#   id_multiplo_25(pokemon)

#3.2
def pokedex_imprimir_pokemon_id_mul_25(pokemones:list):
    '''
    Esta funcion se encarga de imprimir los ID de los pokemones multiplo de 25

    Parametros: Una lista representando a los pokemones
    '''
    for pokemon in pokemones:
        nombre_pokemon = obtener_nombre_pokemon(pokemon)
        id_pokemon = obtener_id_pokemon(pokemon)
        id_25 = id_multiplo_25(pokemon)
        if (id_25 == True):
            print(f"Nombre: {nombre_pokemon} - ID: {id_pokemon}")

#pokedex_imprimir_pokemon_id_mul_25(pokemones)

#---------------------PUNTO 4----------------

#4.1
def nombre_format_pokemon(pokemon:dict) -> str:
    '''
    Esta funcion se encarga de darle un formato al ID y nombre del pokemon

    Parametros: Un diccionario representando al pokemon

    Retorna: Un string con formato (#006 - charizard)
    '''
    nombre_pokemon = obtener_nombre_pokemon(pokemon)
    id_pokemon = obtener_id_pokemon(pokemon)
    id_pokemon = id_pokemon.zfill(3)
    retorno = f"#{id_pokemon} - {nombre_pokemon}" 
    return retorno

#for pokemon in pokemones:
#    print(nombre_format_pokemon(pokemon))

#4.2
def pokedex_imprimir_nombres_poke_fmt(pokemones:list):
    '''
    Esta funcion se encarga de imprimir los nombres de los pokemones con nuevo formato

    Parametros: Una lista representando a los pokemones
    '''
    for pokemon in pokemones:
        retorno = nombre_format_pokemon(pokemon)
        print(retorno)

#pokedex_imprimir_nombres_poke_fmt(pokemones)
      
#---------------------PUNTO 5----------------

#5.1
def calcular_max_dato(pokemones:list,tipo:str,clave:str) -> int:
    '''
    Esta funcion se encarga de saber cual es el dato maximo a analizar

    Parametros: Una lista que representa a los pokemones, 
    un string que toma el valor "maximo" 
    y una clave a analizar

    Retorna: El dato maximo de tipo INT si se puede analizar, un mensaje de error en caso contrario
    '''
    pokemon_max = pokemones[0][clave]
    try:
        for pokemon in pokemones:
            if (int(pokemon_max) < pokemon[clave]):
                pokemon_max = pokemon[clave]
            retorno = pokemon_max
    except:
        retorno = "ERROR! EL DATO NO SE PUEDE ANALIZAR"
    return retorno    


#print(calcular_max_dato(pokemones,"maximo","nombre"))

#5.2
def obtener_lista_pokemones(pokemones:list,clave:str,valor:int) -> list:
    '''
    Esta funcion se encarga de analizar la lista de pokemones y tomar los valores que coincidan

    Parametros: La lista de pokemones,
    La key la cual deberá evaluar cada pokémon que coincida su valor,
    El valor el cual debe evaluar que sea igual.


    Retorna: Una lista con todos los nombres de pokemones que coincidan
    '''
    lista_pokemones = []
    for pokemon in pokemones:
        if (pokemon[clave] == valor):
            lista_pokemones.append(pokemon["nombre"])
        retorno = lista_pokemones
    return retorno

#print(obtener_lista_pokemones(pokemones,"poder",30)) 
 
#5.3
def string_max_dato(pokemones:list,tipo:str,clave:str) -> str:
    '''
    Esta funcion se encarga de analizar la lista de pokemones y tomar los pokemones que cumplan con los requisitos

    Parametros:  La lista de pokemones,
    Un string que representará el máximo,
    Un string que representará el dato/key a calcular

    Retorna: Un string con el valor máximo del dato calculado
    y todos los pokemones que cumplan dicha condición.

    '''
    pokemon_max = calcular_max_dato(pokemones,tipo,clave)
    nombre_pokemon = obtener_lista_pokemones(pokemones,clave,pokemon_max)
    nombres = ""
    for pokemon in nombre_pokemon:
        nombres += pokemon + " - "
    retorno = f"{clave} máximo: {pokemon_max} | Pokemones: {nombres}"

    return retorno
    
#print(string_max_dato(pokemones,"maximo","poder"))

#5.4
def imprimir_pokemones_fuertes(format:str):
    '''
    Esta funcion se encarga de imprimir los pokemones mas fuertes
    '''
    pokemones_mas_fuertes = format
    print(pokemones_mas_fuertes)


#imprimir_pokemones_fuertes(string_max_dato(pokemones,"maximo","poder"))

#5.5
def pokedex_imprimir_pokemones_fuertes(pokemones:list):
    '''
    Esta funcion se encargará de buscar el o los pokemones mas fuertes, 
    formateara el mensaje con todos los que cumplan la condición y los imprimirá.

    Parametros: Una lista que representa a los pokemones
    '''
    pokemones_mas_fuertes = string_max_dato(pokemones,"maximo","poder")
    pokemones_mas_fuertes = f"Pokemones mas fuertes: {pokemones_mas_fuertes[30:]}"
    imprimir_pokemones_fuertes(pokemones_mas_fuertes)

#pokedex_imprimir_pokemones_fuertes(pokemones)  

#---------------------PUNTO 6----------------

#6.1
def calcular_min_dato(pokemones:list,tipo:str,clave:str) -> int:
    '''
    Esta funcion se encarga de saber cual es el dato minimo a analizar

    Parametros: Una lista que representa a los pokemones, 
    un string que toma el valor "minimo" 
    y una clave a analizar

    Retorna: El dato minimo de tipo INT si se puede analizar, un mensaje de error en caso contrario
    '''
    pokemon_min = pokemones[0][clave]
    try:
        for pokemon in pokemones:
            if (int(pokemon_min) > pokemon[clave]):
                pokemon_min = pokemon[clave]
            retorno = pokemon_min
    except:
        retorno = "ERROR! EL DATO NO SE PUEDE ANALIZAR"
    return retorno    

#print(calcular_min_dato(pokemones,"minimo","poder"))

#---------------------PUNTO 7----------------
#---------------------PUNTO 8----------------
#---------------------PUNTO 9----------------
#---------------------PUNTO 10----------------
#---------------------PUNTO 11----------------
#---------------------PUNTO 12----------------
#---------------------PUNTO 13----------------
#---------------------PUNTO 14----------------
#---------------------PUNTO 15----------------
#---------------------PUNTO 16----------------
#---------------------PUNTO 17----------------
#---------------------PUNTO 18----------------