import re

def calcular_nombre_heroes(lista:list):
    for personaje in lista:
        if (personaje["genero"] == "M"):
            print(personaje["nombre"])
                 

def calcular_nombre_heroinas(lista:list):
    for personaje in lista:
        if (personaje["genero"] == "F"):
            print(personaje["nombre"])
      
                             
def buscar_primer_masculino(lista:list):
    personaje_masculino = {}   
    for personaje in lista:
        if(personaje["genero"] == "M"): 
            personaje_masculino = personaje
            break
    
    return personaje_masculino

def buscar_primer_femenino(lista:list):   
    personaje_femenino = {}   
    for personaje in lista:
        if(personaje["genero"] == "F"): 
            personaje_femenino = personaje
            break
    
    return personaje_femenino

def calcular_heroe_mas_alto(lista:list):
    personaje_masculino_mas_alto = buscar_primer_masculino(lista)
    for personaje in lista:
        if (personaje["genero"] == "M"):
            personaje_masculino_mas_alto["altura"] = float(personaje_masculino_mas_alto["altura"])
            personaje["altura"] = float(personaje["altura"])
            if (personaje_masculino_mas_alto["altura"] < personaje["altura"]):
                personaje_masculino_mas_alto = personaje  

    print("\nNombre = {0} - Altura {1}".format(personaje_masculino_mas_alto["nombre"],personaje_masculino_mas_alto["altura"]))


def calcular_heroina_mas_alta(lista:list):
    personaje_femenino_mas_alto = buscar_primer_femenino(lista)
    for personaje in lista:
        if (personaje["genero"] == "F"):
            personaje_femenino_mas_alto["altura"] = float(personaje_femenino_mas_alto["altura"])
            personaje["altura"] = float(personaje["altura"])
            if (personaje_femenino_mas_alto["altura"] < personaje["altura"]):
                personaje_femenino_mas_alto = personaje  

    print("\nNombre = {0} - Altura {1}".format(personaje_femenino_mas_alto["nombre"],personaje_femenino_mas_alto["altura"]))


def calcular_heroe_mas_bajo(lista:list):
    personaje_masculino_mas_bajo = buscar_primer_masculino(lista)
    for personaje in lista:
        if (personaje["genero"] == "M"):
            personaje_masculino_mas_bajo["altura"] = float(personaje_masculino_mas_bajo["altura"])
            personaje["altura"] = float(personaje["altura"])
            if (personaje_masculino_mas_bajo["altura"] > personaje["altura"]):
                personaje_masculino_mas_bajo = personaje  

    print("\nNombre = {0} - Altura {1}".format(personaje_masculino_mas_bajo["nombre"],personaje_masculino_mas_bajo["altura"]))


def calcular_heroina_mas_bajo(lista:list):
    personaje_femenino_mas_bajo = buscar_primer_femenino(lista)
    for personaje in lista:
        if (personaje["genero"] == "F"):
            personaje_femenino_mas_bajo["altura"] = float(personaje_femenino_mas_bajo["altura"])
            personaje["altura"] = float(personaje["altura"])
            if (personaje_femenino_mas_bajo["altura"] > personaje["altura"]):
                personaje_femenino_mas_bajo = personaje  

    print("\nNombre = {0} - Altura {1}".format(personaje_femenino_mas_bajo["nombre"],personaje_femenino_mas_bajo["altura"]))   


def calcular_promedio_altura_masculino(lista:list):
    acumulador_masculino = 0
    contador_masculino = 0
    for personaje in lista:
        if (personaje["genero"] == "M"):
            acumulador_masculino += float(personaje["altura"])
            contador_masculino += 1

    print("\nPromedio de altura: {0}".format(acumulador_masculino / contador_masculino)) 


def calcular_promedio_altura_femenino(lista:list):
    acumulador_femenino = 0
    contador_femenino = 0
    for personaje in lista:
        if (personaje["genero"] == "F"):
            acumulador_femenino += float(personaje["altura"])
            contador_femenino += 1

    print("Promedio de altura: {0}".format(acumulador_femenino / contador_femenino))  
 

def calcular_cantidad_ojos(lista:list):
    colores_de_ojos = []
    for color_ojos in lista:
        colores_de_ojos.append(color_ojos["color_ojos"])

    colores_de_ojos = set(colores_de_ojos)

    lista_colores_ojos = []
    for color in colores_de_ojos:
        dic_color_ojos={"color":color,"cantidad":0}
        for personaje in lista:
            if (personaje["color_ojos"] == color):
                dic_color_ojos["cantidad"] += 1

        lista_colores_ojos.append(dic_color_ojos)        

    for lista in lista_colores_ojos:
        print("Color: {0} - Cantidad: {1}".format(lista["color"],lista["cantidad"]))

def calcular_cantidad_pelo(lista:list):
    colores_de_pelo = []
    for color_pelo in lista:
        colores_de_pelo.append(color_pelo["color_pelo"])

    colores_de_pelo = set(colores_de_pelo)

    lista_colores_de_pelo = []
    for color in colores_de_pelo:
        dic_color_pelo={"color":color,"cantidad":0}
        for personaje in lista:
            if (personaje["color_pelo"] == color):
                dic_color_pelo["cantidad"] += 1

        lista_colores_de_pelo.append(dic_color_pelo)        

    for lista in lista_colores_de_pelo:
        print("Color: {0} - Cantidad: {1}".format(lista["color"],lista["cantidad"]))
    
def calcular_cantidad_inteligencia(lista:list):
    nivel_inteligencia = []
    for inteligencia in lista:
        nivel_inteligencia.append(inteligencia["inteligencia"])

    nivel_inteligencia = set(nivel_inteligencia)

    lista_inteligencia = []
    for nivel in nivel_inteligencia:
        dic_inteligencia={"inteligencia":nivel,"cantidad":0}
        for personaje in lista:
            if (personaje["inteligencia"] == nivel):
                dic_inteligencia["cantidad"] += 1
        lista_inteligencia.append(dic_inteligencia)        
    
    imprimir_lista(lista_inteligencia,"inteligencia")

def imprimir_lista(lista:list,clave:str):
    for dato in lista:
        if (dato[clave] == ""):
            dato[clave] = "No tiene"  
        print("{2} - {0} - Cantidad: {1}".format(dato[clave],dato["cantidad"],clave))  

def agrupar_heroes_por_ojos(lista:list):
    grupo_ojos = []
    for personaje in lista:
        grupo_ojos.append(personaje["color_ojos"])

    grupo_ojos = set(grupo_ojos)

    lista_nombre_por_ojos = []
    for ojos in grupo_ojos:
        dic_ojos = {"ojos":ojos,"heroe":[]}
        for personaje in lista:
            if (personaje["color_ojos"] == ojos):
                dic_ojos["heroe"].append(personaje["nombre"])
        lista_nombre_por_ojos.append(dic_ojos)                

    for lista in lista_nombre_por_ojos:
        print("Color de ojos: {0} - Heroe: {1}".format(lista["ojos"],lista["heroe"]))

def agrupar_heroes_por_pelo(lista:list):    
    grupo_pelo = []
    for personaje in lista:
        grupo_pelo.append(personaje["color_pelo"])

    grupo_pelo = set(grupo_pelo)

    lista_nombre_por_pelo = []
    for pelo in grupo_pelo:
        dic_pelo = {"pelo":pelo,"heroe":[]}
        for personaje in lista:
            if (personaje["color_pelo"] == pelo):
                dic_pelo["heroe"].append(personaje["nombre"])
        lista_nombre_por_pelo.append(dic_pelo)                

    for lista in lista_nombre_por_pelo:
        if (lista["pelo"] == ""):
            lista["pelo"] = "Sin pelo"
        print("Color de pelo: {0} - Heroe: {1}".format(lista["pelo"],lista["heroe"]))

def agrupar_heroes_por_inteligencia(lista:list):
    grupo_inteligencia = []
    for personaje in lista:
        grupo_inteligencia.append(personaje["inteligencia"])

    grupo_inteligencia = set(grupo_inteligencia)

    lista_nombre_por_inteligencia = []
    for nivel in grupo_inteligencia:
        dic_inteligencia = {"nivel":nivel,"heroe":[]}
        for personaje in lista:
            if (personaje["inteligencia"] == nivel):
                dic_inteligencia["heroe"].append(personaje["nombre"])
        lista_nombre_por_inteligencia.append(dic_inteligencia)                

    for lista in lista_nombre_por_inteligencia:
        if (lista["nivel"] == ""):
            lista["nivel"] = "No tiene"
        print("Inteligencia: {0} - Heroe: {1}".format(lista["nivel"],lista["heroe"]))
  
def imprimir_menu_principal():
    print("\n\n Opciones: \n"
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

def obtener_valor_opcion():
    imprimir_menu_principal()
    opcion = input("Ingrese una opcion: ")
    opcion = opcion[0]
    opcion = opcion.upper()
    validacion = re.search("[A-NZ]",opcion)
    if (validacion == None):
        retorno = -1
    else:
        retorno = opcion
    return retorno
