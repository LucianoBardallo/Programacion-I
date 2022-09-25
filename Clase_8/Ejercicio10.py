
import re
import json

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
        print("\n---Datos normalizados---\n") 


def imprimir_dato(dato:str):
    '''
    Imprime un dato del tipo string pasado por parametro
    '''
    print(dato)

def dividir(dividendo:int,divisor:int):
    '''
    Esta funcion se encarga de dividir

    Parametros: Recibe un numero que representa el dividendo y otro que representa el divisor

    Retorna el resultado de la division o un (0) en caso de no poder hacerse
    '''
    if (divisor == 0):
        return 0
    else:
        division = dividendo // divisor
        return division

#---------------------PUNTO 1----------------

#1.1
def imprimir_menu_desafio_5():
    imprimir_dato("        \n ---- OPCIONES ---- \n"
                   " A = Lista de Heroes  \n"
                   " B = Lista de Heroinas \n"
                   " C = Heroe mas alto\n"
                   " D = Heroina mas alta\n"
                   " E = Heroe mas bajo\n"
                   " F = Heroina mas baja\n"
                   " G = Promedio de altura masculino\n"
                   " H = Promedio de altura femenino\n"
                   " I = Cantidad color de ojos\n"
                   " J = Cantidad color de pelo\n"
                   " K = Cantidad nivel de inteligencia\n"
                   " L = Grupo de Heroes por color de ojos\n"
                   " M = Grupo de Heroes por color de pelo\n"
                   " N = Grupo de Heroes por tipo de inteligencia\n"
                   " Z = Salir del programa\n")

#imprimir_menu_desafio_5()      


#1.2
def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    opcion = input(" >")
    opcion = opcion[0]
    opcion = opcion.upper()
    validacion = re.search("[A-NZ]",opcion)
    if (validacion == None):
        retorno = -1
    else:
        retorno = opcion
    return retorno

#print(stark_menu_principal_desafio_5())

#1.3
def stark_marvel_app_5(lista_heroes:list):
    opcion = stark_menu_principal_desafio_5()
    
#stark_marvel_app_5(lista_personajes)

#1.4
def leer_archivo(nombre_archivo:str)->list:
    dic_json = {}
    with open(nombre_archivo,"r") as archivo:
        dic_json = json.load(archivo)
    return dic_json["heroes"]

#for personaje in lista_personajes:
#    print("\n")
#    print(personaje)
lista_personajes = leer_archivo("Clase_8\data_stark.json")
stark_normalizar_datos(lista_personajes)

#1.5
def guardar_archivo(archivo_a_guardar:str,archivo_contenido:str):

    validacion = re.search("(.json|.csv)$",archivo_a_guardar)
    if (validacion == None):
        mensaje = f"Error al crear el archivo: {archivo_a_guardar}"
        retorno = False
    else:
        validacion = re.search("(.json)$",archivo_a_guardar)
        with open(archivo_a_guardar,"w+") as archivo:
            archivo_almacenado = archivo.write(archivo_contenido)
        if (validacion == None):
            mensaje = f"Se creó el archivo: {archivo_a_guardar}"
        else:
            mensaje = f"Se creó el archivo: {archivo_a_guardar}"
        print(mensaje)
        retorno = True
    return retorno

#guardar_archivo("Clase_8\data_nueva.json","Prueba")

#1.6
def capitalizar_palabras(dato:str):
    dato_nuevo = set(re.findall("[a-zA-Z]+",dato))
    for palabra in dato_nuevo:
        palabra_cap = palabra.capitalize()
        dato = re.sub(palabra,palabra_cap,dato)
    return dato

#print(capitalizar_palabras("233hola 233hola chau321"))

#1.7
def obtener_nombre_capitalizado(heroe:dict):
    nombre = capitalizar_palabras(heroe["nombre"])
    nombre_heroe = f"Nombre: {nombre}"
    return nombre_heroe
    
#print(obtener_nombre_capitalizado(lista_personajes[0]))

#1.8
def obtener_nombre_y_dato(heroe:dict,key:str) -> str:
    nombre = obtener_nombre_capitalizado(heroe)
    dato = heroe[key]
    key = key.capitalize()
    nombre_mas_dato = f"{nombre} | {key}: {dato} "
    return nombre_mas_dato

#print(obtener_nombre_y_dato(lista_personajes[0],"fuerza"))

#---------------------PUNTO 2----------------

#2.1
def es_genero(heroe:dict,genero:str) -> bool:
    retorno = False
    genero = genero.upper()
    if (genero == heroe["genero"]):
        retorno = True
    return retorno

#print(es_genero(lista_personajes[0],"F"))

#2.2
def stark_guardar_heroe_genero(lista_heroes:list,genero:str):
    heroes = ""
    for heroe in lista_heroes:
        validacion = es_genero(heroe,genero)
        if (validacion == True):
            nombre = obtener_nombre_capitalizado(heroe)
            print(nombre)
            nombre = nombre.replace("Nombre: ","")
            heroes += nombre + ","

            
    guardar_archivo("Clase_8\personajes.csv",heroes)  
    

#stark_guardar_heroe_genero(lista_personajes,"f")

#---------------------PUNTO 3----------------

#3.1
def calcular_min_genero(lista_heroes:list,key:str,genero:str) -> str:
    flag = False
    for heroe in lista_heroes:
        if(flag == False or float(heroe[key]) < minimo):
            validacion = es_genero(heroe,genero)
            if(validacion == True):
                minimo = float(heroe[key])
                heroe_minimo = f"{obtener_nombre_y_dato(heroe,key)}"
                flag = True
    return heroe_minimo

#print(calcular_min_genero(lista_personajes,"fuerza","M"))

#3.2
def calcular_max_genero(lista_heroes:list,key:str,genero:str) -> str:
    flag = False
    for heroe in lista_heroes:
        if(flag == False or float(heroe[key]) > maximo):
            validacion = es_genero(heroe,genero)
            if(validacion == True):
                maximo = float(heroe[key])
                heroe_maximo = f"{obtener_nombre_y_dato(heroe,key)}"
                flag = True
    return heroe_maximo

#print(calcular_max_genero(lista_personajes,"altura","M"))

#3.3
def calcular_max_min_dato(lista_heroes:list,key:str,genero:str,tipo:str) -> str:
    tipo = tipo.lower()
    if(tipo == "maximo"):
        retorno = calcular_max_genero(lista_heroes,key,genero)
    elif(tipo == "minimo"):
        retorno = calcular_min_genero(lista_heroes,key,genero)
    return retorno

#print(calcular_max_min_dato(lista_personajes,"altura","M","minimo"))   

#3.4
def stark_calcular_imprimir_guardar_heroe_genero(lista_heroes:list,key:str,genero:str,tipo:str):
    heroe = calcular_max_min_dato(lista_heroes,key,genero,tipo)
    tipo = tipo.lower()
    if (tipo == "minimo"):
        principio = "Menor"
    elif (tipo == "maximo"):
        principio = "Mayor"
    nombre_formato = f"{principio} {key}: {heroe}"
    nombre_formato = capitalizar_palabras(nombre_formato)
    imprimir_dato(nombre_formato)
    try:
        guardar_archivo(f"Clase_8\heroes_{tipo}_{key}_{genero}.csv",nombre_formato)
        retorno = True
    except:
        retorno = False
    return retorno

#stark_calcular_imprimir_guardar_heroe_genero(lista_personajes,"peso","M","maximo")
#---------------------PUNTO 4----------------

#4.1
def sumar_dato_heroe_genero(lista_heroes:list,key:str,genero:str):
    try:
        lista_suma = []
        for heroe in lista_heroes:
            flag = True
            if (type(heroe) == type({}) and len(heroe) > 0 and heroe["genero"] == genero):
                if (flag == True and type(heroe[key]) == type(str())):
                    suma = ""
                    flag = False
                elif(flag == True and type(heroe[key]) == type(int())):
                    suma = 0
                    flag = False
                elif(flag == True and type(heroe[key]) == type(float())):
                    suma = 0.0
                    flag = False
                lista_suma.append(heroe[key])  

        for heroe in lista_suma:
            if (type(heroe) == type(str())):
                suma += " "
            suma += heroe
        retorno = suma
    except:
        retorno = -1               
    return retorno

#print(sumar_dato_heroe_genero(lista_personajes,"fuerza","F"))

#4.2
def cantidad_heroes_genero(lista_heroes:list,genero:str):
    cantidad = 0
    for heroe in lista_heroes:
        if (heroe["genero"] == genero):
            cantidad += 1
    return cantidad

#print(cantidad_heroes_genero(lista_personajes,"F"))

#4.3
def calcular_promedio_genero(lista_heroes:list,key:str,genero:str):
    suma = sumar_dato_heroe_genero(lista_heroes,key,genero)
    cantidad = cantidad_heroes_genero(lista_heroes,genero)
    retorno = dividir(suma,cantidad)
    return retorno

#print(calcular_promedio_genero(lista_personajes,"fuerza","F"))

#4.4
def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes:list,genero:str):
    if (len(lista_heroes) > 0):
        altura_promedio = calcular_promedio_genero(lista_heroes,"altura",genero)
        contenido = "Altura promedio de genero {1}: {0}".format(altura_promedio,genero)
        imprimir_dato(contenido)
        guardar_archivo(f"Clase_8\heroes_promedio_altura_{genero}.csv",contenido)
        retorno = True
    else:
        imprimir_dato("Error: Lista de héroes vacia")
        retorno = False
    return retorno

#stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes,"M")

#---------------------PUNTO 5----------------

#5.1
def calcular_cantidad_tipo(lista_heroes:list,key:str):
    if (len(lista_heroes) > 0):
        lista_agrupacion = []
        for personaje in lista_personajes:
            personaje[key] = capitalizar_palabras(personaje[key])
            lista_agrupacion.append(personaje[key])
        

        lista_agrupacion = set(lista_agrupacion)
        #print(lista_agrupacion)
        
        lista_resultado = []
        for dato in lista_agrupacion:
            dic_cantidad = {dato:0}
            for personaje in lista_personajes:
                personaje[key] = capitalizar_palabras(personaje[key])
                if (personaje[key] == dato):
                    dic_cantidad[dato] += 1
            lista_resultado.append(dic_cantidad)

        retorno = lista_resultado
    else:
        dic_error = {"Error": "La lista se encuentra vacia"}
        retorno = dic_error
    return retorno

cantidad_tipo = calcular_cantidad_tipo(lista_personajes,"color_ojos")
print(cantidad_tipo)

#5.2
def guardar_cantidad_heroes_tipo(dic_heroe:dict,key:str):
    for elemento in dic_heroe:
        print(elemento)

#guardar_cantidad_heroes_tipo(cantidad_tipo,"color_pelo")
#---------------------PUNTO 6----------------