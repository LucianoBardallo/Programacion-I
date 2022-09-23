from data_stark import lista_personajes

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

#---------------------PUNTO 2----------------

def obtener_nombre_y_dato(dic:dict,key:str)->str:
    '''
    Esta funcion se encarga de buscar el nombre y el atributo a eleccion en un diccionario e imprimirlo

    Parametros: Dic de tipo dictionary - Key de tipo string

    Retorna un string con este formato de ej: "Nombre: (Heroe) - (Atributo): (Numero del atributo)"
    '''
    nombre_y_dato = "Nombre: {0} | {1}: {2}".format(dic["nombre"],key,dic[key])

    return nombre_y_dato

#---------------------PUNTO 3----------------

def stark_imprimir_nombres_alturas(lista:list):
    '''
    Esta funcion se encarga de imprimir el nombre y la altura de los heroes en forma de lista

    Parametros: Recibe una lista de tipo list.

    Retorna -1 si la lista esta vacia
    '''
    if (len(lista) > 0):
        for indice in range(len(lista)):
            imprimir_dato(obtener_nombre_y_dato(lista[indice],"altura"))
    else:
        return -1

#---------------------PUNTO 4----------------

#4.1
def calcular_max(lista:list,key:str)->str:
    '''
    Esta funcion se encarga de calcular un dato maximo de una lista

    Parametros: Recibirá por parámetro una lista y 
    una key (string) la cual representará el dato que deberá ser evaluado

    Retorna una variable str con la estructura Nombre: (Heroe) // key: (key)
    '''
    flag = False
    for heroe in lista:
        if(flag == False or heroe[key] > maximo):
            maximo = heroe[key]
            heroe_maximo = f"{obtener_nombre(heroe)} // {key}: {heroe[key]}"
            flag = True
    return heroe_maximo

#4.2
def calcular_min(lista:list,key:str)->str:
    '''
    Esta funcion se encarga de calcular un dato minimo de una lista

    Parametros: Recibirá por parámetro una lista y 
    una key (string) la cual representará el dato que deberá ser evaluado

    Retorna una variable str con la estructura Nombre: (Heroe) // key: (key)
    '''
    flag = False
    for heroe in lista:
        if(flag == False or heroe[key] < minimo):
            minimo = heroe[key]
            heroe_minimo = f"{obtener_nombre(heroe)} // {key}: {heroe[key]}"
            flag = True
    return heroe_minimo

#4.3
def calcular_max_min_dato(lista:list,tipo:str,key:str):
    '''
    Esta funcion se encarga de calcular un dato minimo o maximo de una lista

    Parametros: Recibirá por parámetro una lista,
    un tipo (maximo-minimo) y una key (string) la cual representará el dato que deberá ser evaluado

    Retorna una variable con el dato maximo o minimo del heroe elegido
    '''
    heroe_max_min = lista[0]
    for heroe in lista:
        if (tipo == "maximo"):
            heroe_max_min = calcular_max(lista,key)
        elif(tipo == "minimo"):    
            heroe_max_min = calcular_min(lista,key)     
    return heroe_max_min

#4.4
def stark_calcular_imprimir_heroe(lista:list,tipo:str,key:str):
    '''
    Esta funcion se encarga de calcular e imprimir el heroe con su valor adecuado

    Parametros: Recibe una lista, el tipo (maximo-minimo) y
    una key que representa el dato a ser evaluado

    Imprime el nombre y el valor calculado
    '''
    if (len(lista) > 0):
        retorno = calcular_max_min_dato(lista,tipo,key)
    else:
        retorno = -1
    return retorno   

#---------------------PUNTO 5----------------

#5.1
def sumar_dato_heroe(lista:list,key:str):
    '''
    Esta funcion se encarga de sumar los datos de la key pasada por parametro

    Parametros: Recibe una lista y una key que representa el dato a ser sumado

    Retorna la suma del dato evaluado
    '''
    lista_suma = []
    flag = True
    for dato in lista:
        if (flag == True and type(dato[key]) == type(str())):
            suma = ""
            flag = False
        elif(flag == True and type(dato[key]) == type(int())):
            suma = 0
            flag = False
        elif(flag == True and type(dato[key]) == type(float())):
            suma = 0.0
            flag = False
        if (type(dato) == type({}) and len(dato) > 0):
            suma = dato[key]
        lista_suma.append(suma)  

    for dato in lista_suma:
        if (type(dato) == type(str())):
            suma += " "
        suma += dato
                   
    return suma

#5.2
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

#5.3
def calcular_promedio(lista:list,key:str):
    '''
    Esta funcion se encarga de calcular el promedio

    Parametros: Recibe una lista y una key que representa el dato a ser promediado

    Retorna el promedio del dato pasado por parámetro
    '''
    suma = sumar_dato_heroe(lista,key)
    retorno = dividir(suma,len(lista))
    return retorno

#5.4
def stark_calcular_imprimir_promedio_altura(lista:list):
    '''
    Esta funcion se encarga de calcular e imprimir el promedio de altura de una lista

    Parametros: Recibe una lista

    Retorna el promedio de altura entre todos los datos de la lista
    '''
    if (len(lista) == 0):
        return -1
    altura_promedio = calcular_promedio(lista,"altura")
    imprimir_dato("Altura promedio de heroes: {0}".format(altura_promedio))

#---------------------PUNTO 6----------------

#6.1
def imprimir_menu():
    '''
    Esta funcion imprime una estructura de menu
    '''
    imprimir_dato("\n Opciones: \n"
        " 1 = Obtener nombre\n"
        " 2 = Imprimir lista de nombres\n"
        " 3 = Obtener nombre y dato\n"
        " 4 = Imprimir nombre y altura\n"
        " 5 = Calcular maximo o minimo\n"
        " 6 = Imprimir nombre y maximo o minimo\n"
        " 7 = Sumar dato de heroe\n"
        " 8 = Calcular promedio\n"
        " 9 = Salir\n")

#6.2
def validar_entero(numero:str):
    '''
    Esta funcion valida un numero para ser entero

    Parametros: Recibe un numero del dato (string)

    Retorna un booleano, True si se puede pasar a entero, False si no se puede
    '''
    try:
        if(type(float(numero)) == type(float()) or type(int(numero)) == type(int())):
            retorno = True
    except:
        retorno = False
    return retorno

#6.3
def stark_menu_principal():
    '''
    Esta funcion se encarga de imprimir el menu y tomar un dato del usuario por parametro y validarlo

    Retorna -1 si no se puede hacer y el numero entero si se puede
    '''
    imprimir_menu()
    opcion = input("Ingrese una opcion: ")
    validacion = validar_entero(opcion)
    retorno = -1
    if (validacion == True):
        retorno = int(opcion)
    return retorno

#---------------------PUNTO 7----------------

def stark_marvel_app(lista:list):
    '''
    Esta funcion se encarga de mostrar el menu y dejar al usuario interactuar con todas las opciones

    Parametros: Recibe una lista
    '''
    while True:
        opcion = stark_menu_principal()
        if (opcion == 1):
            posicion = input("Ingrese una posicion de la lista: ")
            posicion = int(posicion)
            print(obtener_nombre(lista[posicion]))
        elif(opcion == 2):  
            stark_imprimir_nombres_heroes(lista)
        elif(opcion == 3): 
            posicion = input("Ingrese una posicion de la lista: ")
            posicion = int(posicion) 
            key = input("Ingrese la clave a evaluar: ")
            print(obtener_nombre_y_dato(lista[posicion],key))
        elif(opcion == 4):  
            stark_imprimir_nombres_alturas(lista)
        elif(opcion == 5):
            key = input("Ingrese la clave a evaluar: ") 
            tipo = input("Ingrese el tipo (maximo-minimo): ") 
            print(calcular_max_min_dato(lista,tipo,key))
        elif(opcion == 6):  
            key = input("Ingrese la clave a evaluar: ") 
            tipo = input("Ingrese el tipo (maximo-minimo): ")
            print(stark_calcular_imprimir_heroe(lista,tipo,key))
        elif(opcion == 7): 
            key = input("Ingrese la clave a evaluar: ") 
            print(sumar_dato_heroe(lista,key))
        elif(opcion == 8):  
            key = input("Ingrese la clave a evaluar: ") 
            print(calcular_promedio(lista,key))
        elif(opcion == 9):
            break                             

stark_marvel_app(lista_personajes)
