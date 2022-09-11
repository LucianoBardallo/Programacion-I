from data_stark import lista_personajes

'''
lista_heroes =
[
 {
   "nombre": "Howard the Duck",
   "identidad": "Howard (Last name unrevealed)",
   "empresa": "Marvel Comics",
   "altura": "79.349999999999994",
   "peso": "18.449999999999999",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Yellow",
   "fuerza": "2",
   "inteligencia": "average"
 },
 {
   "nombre": "Rocket Raccoon",
   "identidad": "Rocket Raccoon",
   "empresa": "Marvel Comics",
   "altura": "122.77",
   "peso": "25.73",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Brown",
   "fuerza": "5",
   "inteligencia": "average"
 }
]

'''
#---------------------PUNTO 0----------------
def stark_normalizar_datos(lista:list):
    cambio = False
    for indice in range(len(lista)):
        for clave in lista[indice]:
            if (len(lista) > 0):
                if(type(clave) == type("") and type(clave) != type(float()) and type(clave) != type(int())):
                    if (clave == "altura" or clave == "peso"):
                        cambio = True
                        lista[indice][clave] = float(lista[indice][clave])
                    elif (clave == "fuerza"):
                        lista[indice][clave] = int(lista[indice][clave]) 
            else:
                print("\nError: Lista de heroes vacia")   
    if (cambio == True):
        print("\nDatos normalizados") 

stark_normalizar_datos(lista_personajes)

#---------------------PUNTO 1----------------

#1.1
def obtener_nombre(dic:dict)->str:
    '''
    Obtiene el nombre del heroe seleccionado en el diccionario

    Parametros: Recibe un diccionario de un heroe

    Retorna: Un string formateado de la siguiente manera: "Nombre: (Heroe)"
    '''
    for dato in dic:
        nombre = f"Nombre: {dic[dato]}"
        return nombre


#print(obtener_nombre(lista_personajes[0]))

#1.2
def imprimir_dato(dato:str):
    '''
    Imprime un dato del tipo string pasado por parametro
    '''
    print(dato)

#1.3
def stark_imprimir_nombres_heroes(lista:list):
    '''
    Recibe una lista de heroes y despues la imprime en la consola los nombres de los heroes
    
    Parametros: Recibe la lista de hereos

    Retorna: Inprime una una lista de nombres o retorna -1
    '''
    if (len(lista) > 0):
        for indice in range(len(lista)):
            imprimir_dato(obtener_nombre(lista[indice]))
    else:
        return -1

#stark_imprimir_nombres_heroes(lista_personajes)

#---------------------PUNTO 2----------------

def obtener_nombre_y_dato(dic:dict,key:str)->str:
    '''
    Esta funcion se encarga de buscar el nombre y el atributo a eleccion en un diccionario e imprimirlo

    Parametros: Dic de tipo dictionary - Key de tipo string

    Retorna un string con este formato de ej: "Nombre: (Heroe) - (Atributo): (Numero del atributo)"
    '''
    nombre_y_dato = "Nombre: {0} | {1}: {2}".format(dic["nombre"],key,dic[key])

    return nombre_y_dato

#print(obtener_nombre_y_dato(lista_personajes[3],"fuerza"))

#---------------------PUNTO 3----------------

def stark_imprimir_nombres_alturas(lista:list):
    if (len(lista) > 0):
        for indice in range(len(lista)):
            imprimir_dato(obtener_nombre_y_dato(lista[indice],"altura"))
    else:
        return -1

#stark_imprimir_nombres_alturas(lista_personajes)

#---------------------PUNTO 4----------------

#4.1
def calcular_max(lista:list,key:str)->str:
    flag = False
    for heroe in lista:
        if(flag == False or heroe[key] > maximo):
            maximo = heroe[key]
            heroe_maximo = f"{obtener_nombre(heroe)} // {key}: {heroe[key]}"
            flag = True
    return heroe_maximo

#print(calcular_max(lista_personajes,"altura"))

#4.2
def calcular_min(lista:list,key:str)->str:
    flag = False
    for heroe in lista:
        if(flag == False or heroe[key] < minimo):
            minimo = heroe[key]
            heroe_minimo = f"{obtener_nombre(heroe)} // {key}: {heroe[key]}"
            flag = True
    return heroe_minimo
 
#print(calcular_min(lista_personajes,"altura"))

#4.3
def calcular_max_min_dato(lista:list,tipo:str,key:str):
    heroe_max_min = lista[0]
    for heroe in lista:
        if (tipo == "maximo"):
            heroe_max_min = calcular_max(lista,key)
        elif(tipo == "minimo"):    
            heroe_max_min = calcular_min(lista,key)     
    return heroe_max_min

'''
minimo_peso = calcular_max_min_dato(lista_personajes,"minimo","peso")
maximo_peso = calcular_max_min_dato(lista_personajes,"maximo","peso")
minimo_altura = calcular_max_min_dato(lista_personajes,"minimo","altura")
maximo_altura = calcular_max_min_dato(lista_personajes,"maximo","altura")
minimo_fuerza = calcular_max_min_dato(lista_personajes,"minimo","fuerza")
maximo_fuerza = calcular_max_min_dato(lista_personajes,"maximo","fuerza")

print("Maximo: [{0}] || Minimo: [{1}]".format(maximo_altura,minimo_altura))
'''
#4.4
def stark_calcular_imprimir_heroe(lista:list,tipo:str,key:str):
    if (len(lista) > 0):
        retorno = calcular_max_min_dato(lista,tipo,key)
    else:
        retorno = -1
    return retorno   

#print(stark_calcular_imprimir_heroe(lista_personajes,"maximo","altura"))

#---------------------PUNTO 5----------------
    

#---------------------PUNTO 6----------------