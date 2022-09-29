import json
import re

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
        retorno = 0
    else:
        division = dividendo // divisor
        retorno = division
    return retorno
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
                   " I = Nombre de superheroe asociado a los datos anteriores\n"
                   " J = Cantidad color de ojos\n"
                   " K = Cantidad color de pelo\n"
                   " L = Cantidad nivel de inteligencia\n"
                   " M = Grupo de Heroes por color de ojos\n"
                   " N = Grupo de Heroes por color de pelo\n"
                   " O = Grupo de Heroes por tipo de inteligencia\n"
                   " Z = Salir del programa\n")

#1.2
def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    opcion = input("Ingrese una opcion: ")
    opcion = opcion[0]
    opcion = opcion.upper()
    validacion = re.search("[A-OZ]",opcion)
    if (validacion == None):
        retorno = -1
    else:
        retorno = opcion
    return retorno

#1.4
def leer_archivo(nombre_archivo:str)->list:
    dic_json = {}
    with open(nombre_archivo,"r") as archivo:
        dic_json = json.load(archivo)
    return dic_json["heroes"]

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

#1.6
def capitalizar_palabras(dato:str):
    dato_nuevo = set(re.findall("[a-zA-Z]+",dato))
    for palabra in dato_nuevo:
        palabra_cap = palabra.capitalize()
        dato = re.sub(palabra,palabra_cap,dato)
    return dato

#1.7
def obtener_nombre_capitalizado(heroe:dict):
    nombre = capitalizar_palabras(heroe["nombre"])
    nombre_heroe = f"Nombre: {nombre}"
    return nombre_heroe

#1.8
def obtener_nombre_y_dato(heroe:dict,key:str) -> str:
    nombre = obtener_nombre_capitalizado(heroe)
    dato = heroe[key]
    key = key.capitalize()
    nombre_mas_dato = f"{nombre} | {key}: {dato} "
    return nombre_mas_dato

#---------------------PUNTO 2----------------

#2.1
def es_genero(heroe:dict,genero:str) -> bool:
    retorno = False
    genero = genero.upper()
    if (genero == heroe["genero"]):
        retorno = True
    return retorno


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

            
    guardar_archivo("Clase_8\Ejercicio10\personajes.csv",heroes)  

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


#3.3
def calcular_max_min_dato(lista_heroes:list,key:str,genero:str,tipo:str) -> str:
    tipo = tipo.lower()
    if(tipo == "maximo"):
        retorno = calcular_max_genero(lista_heroes,key,genero)
    elif(tipo == "minimo"):
        retorno = calcular_min_genero(lista_heroes,key,genero)
    return retorno
 

#3.4
def stark_calcular_imprimir_guardar_heroe_genero(lista_heroes:list,key:str,genero:str,tipo:str):
    tipo = tipo.lower()
    heroe = calcular_max_min_dato(lista_heroes,key,genero,tipo)
    if (tipo == "minimo"):
        principio = "Menor"
    elif (tipo == "maximo"):
        principio = "Mayor"
    nombre_formato = f"{principio} {key}: {heroe}"
    nombre_formato = capitalizar_palabras(nombre_formato)
    imprimir_dato(nombre_formato)
    try:
        guardar_archivo(f"Clase_8\Ejercicio10\heroes_{tipo}_{key}_{genero}.csv",nombre_formato)
        retorno = True
    except:
        retorno = False
    return retorno

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

#4.2
def cantidad_heroes_genero(lista_heroes:list,genero:str):
    cantidad = 0
    for heroe in lista_heroes:
        if (es_genero(heroe,genero)):
            cantidad += 1
    return cantidad



#4.3
def calcular_promedio_genero(lista_heroes:list,key:str,genero:str):
    suma = sumar_dato_heroe_genero(lista_heroes,key,genero)
    cantidad = cantidad_heroes_genero(lista_heroes,genero)
    retorno = dividir(suma,cantidad)
    return retorno

#4.4
def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes:list,genero:str):
    if (len(lista_heroes) > 0):
        altura_promedio = calcular_promedio_genero(lista_heroes,"altura",genero)
        contenido = "Altura promedio de genero {1}: {0}".format(altura_promedio,genero)
        imprimir_dato(contenido)
        guardar_archivo(f"Clase_8\Ejercicio10\heroes_promedio_altura_{genero}.csv",contenido)
        retorno = True
    else:
        imprimir_dato("Error: Lista de héroes vacia")
        retorno = False
    return retorno

#---------------------PUNTO 5----------------

#5.1
def calcular_cantidad_tipo(lista_heroes:list,key:str):
    try:
        if (len(lista_heroes) > 0):
            lista_agrupacion = []
            for personaje in lista_heroes:
                if(type(personaje[key]) == type(str())):
                    personaje[key] = capitalizar_palabras(personaje[key])
                lista_agrupacion.append(personaje[key])
        
            lista_agrupacion = set(lista_agrupacion)
            lista_agrupacion = list(lista_agrupacion)

            lista_resultado = []
            for dato in lista_agrupacion:
                dic_dato = {dato:0}
                for personaje in lista_heroes:
                    if (personaje[key] == dato):
                        dic_dato[dato] += 1
                lista_resultado.append(dic_dato)  

            dic_resultado = {}
            for dato in lista_resultado:
                dic_resultado = dic_resultado | dato
                
            retorno = dic_resultado
        else:
            dic_error = {"Error": "La lista se encuentra vacia"}
            retorno = dic_error
        
    except:
        retorno = "La key no puede ser evaluada"
    return retorno


#5.2
def guardar_cantidad_heroes_tipo(dic_heroe:dict,key:str):
    try:
        mensaje = ""
        for elemento in dic_heroe:
            mensaje += "Caracteristica: {0} - {1} - Cantidad de Heroes - {2}\n".format(key,elemento,dic_heroe[elemento])
        print(mensaje)
        guardar_archivo(f"Clase_8\Ejercicio10\heroes_cantidad_{key}.csv",mensaje)
        retorno = True
    except:
        retorno = False
    return retorno


#5.3
def stark_calcular_cantidad_por_tipo(lista_heroes:list,key:str):
    try:
        dic_cantidad = calcular_cantidad_tipo(lista_heroes,key)
        guardar_cantidad_heroes_tipo(dic_cantidad,key)
        retorno = True
    except:
        retorno = False
    return retorno


#---------------------PUNTO 6----------------

#6.1
def obtener_lista_de_tipos(lista_heroes:list,key:str):
    lista_nueva = []
    for heroe in lista_heroes:
        if (heroe[key] == ""):
            heroe[key] = "N/A"
        heroe[key] = capitalizar_palabras(heroe[key])
        lista_nueva.append(heroe[key])
    lista_nueva = set(lista_nueva)
    return lista_nueva


#6.2
def normalizar_dato(dato,default="N/A"):
    dato = str(dato)
    if(len(dato) > 0):
        retorno = dato
    else:
        retorno = default
    return retorno
    

#6.3
def normalizar_heroe(dic_heroe:dict,key:str):
    heroe = normalizar_dato(dic_heroe[key])
    heroe = capitalizar_palabras(heroe)
    
    return heroe

#6.4
def obtener_heroes_por_tipo(lista_heroes:list,lista_set:set,key:str):
    lista_nombre_por_key = []
    for clave in lista_set: 
        dic_ojos = {clave:[]}
        for personaje in lista_heroes:
            normalizar_heroe(personaje,key)
            if (personaje[key] == clave):
                personaje["nombre"] = normalizar_heroe(personaje,"nombre")
                dic_ojos[clave].append(personaje["nombre"])
        lista_nombre_por_key.append(dic_ojos) 

    dic_ordenado = {}
    for elemento in lista_nombre_por_key:
        dic_ordenado = dic_ordenado | elemento

    return dic_ordenado

#6.5
def guardar_heroes_por_tipo(dic_valor:dict,key:str):
    try:
        lista_nueva = []
        for dato in dic_valor:
            cadena = " | "
            cadena = cadena.join(dic_valor[dato])
            mensaje = "{0} - {1}: {2}".format(key,dato,cadena)
            lista_nueva.append(mensaje)
            imprimir_dato(mensaje)

        separador = "\n"
        separador = separador.join(lista_nueva)
        guardar_archivo(f"Clase_8\Ejercicio10\heroes_segun_{key}.csv",separador)
        retorno = True
    except:
        retorno = False
    return retorno


def stark_listar_heroes_por_dato(lista_heroes:list,key:str):
    lista_seteada = obtener_lista_de_tipos(lista_heroes, key)
    dic_nuevo = obtener_heroes_por_tipo(lista_heroes, lista_seteada, key)
    validacion = guardar_heroes_por_tipo(dic_nuevo, key)
    if (validacion == True):
        retorno = True
    else:
        retorno = False
    return retorno
