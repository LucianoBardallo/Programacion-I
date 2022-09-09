from data_stark import lista_personajes

def calcular_nombre_heroes():
    print("---Heroes---")
    for personaje in lista_personajes:
        if (personaje["genero"] == "M"):
            print(personaje["nombre"])
            
    print("-------------------------------------\n")        

def calcular_nombre_heroinas():
    print("---Heroinas---")
    for personaje in lista_personajes:
        if (personaje["genero"] == "F"):
            print(personaje["nombre"])

    print("-------------------------------------\n")            
                             
def buscar_primer_masculino():
    personaje_masculino = {}   
    for personaje in lista_personajes:
        if(personaje["genero"] == "M"): 
            personaje_masculino = personaje
            break
    
    return personaje_masculino

def buscar_primer_femenino():   
    personaje_femenino = {}   
    for personaje in lista_personajes:
        if(personaje["genero"] == "F"): 
            personaje_femenino = personaje
            break
    
    return personaje_femenino

def calcular_heroe_mas_alto():
    personaje_masculino_mas_alto = buscar_primer_masculino()
    for personaje in lista_personajes:
        if (personaje["genero"] == "M"):
            personaje_masculino_mas_alto["altura"] = float(personaje_masculino_mas_alto["altura"])
            personaje["altura"] = float(personaje["altura"])
            if (personaje_masculino_mas_alto["altura"] < personaje["altura"]):
                personaje_masculino_mas_alto = personaje  

    print("\nNombre = {0} - Altura {1}".format(personaje_masculino_mas_alto["nombre"],personaje_masculino_mas_alto["altura"]))

    print("-------------------------------------\n") 

def calcular_heroina_mas_alta():
    personaje_femenino_mas_alto = buscar_primer_femenino()
    for personaje in lista_personajes:
        if (personaje["genero"] == "F"):
            personaje_femenino_mas_alto["altura"] = float(personaje_femenino_mas_alto["altura"])
            personaje["altura"] = float(personaje["altura"])
            if (personaje_femenino_mas_alto["altura"] < personaje["altura"]):
                personaje_femenino_mas_alto = personaje  

    print("\nNombre = {0} - Altura {1}".format(personaje_femenino_mas_alto["nombre"],personaje_femenino_mas_alto["altura"]))

    print("-------------------------------------\n") 

def calcular_heroe_mas_bajo():
    personaje_masculino_mas_bajo = buscar_primer_masculino()
    for personaje in lista_personajes:
        if (personaje["genero"] == "M"):
            personaje_masculino_mas_bajo["altura"] = float(personaje_masculino_mas_bajo["altura"])
            personaje["altura"] = float(personaje["altura"])
            if (personaje_masculino_mas_bajo["altura"] > personaje["altura"]):
                personaje_masculino_mas_bajo = personaje  

    print("\nNombre = {0} - Altura {1}".format(personaje_masculino_mas_bajo["nombre"],personaje_masculino_mas_bajo["altura"]))

    print("-------------------------------------\n") 

def calcular_heroina_mas_bajo():
    personaje_femenino_mas_bajo = buscar_primer_femenino()
    for personaje in lista_personajes:
        if (personaje["genero"] == "F"):
            personaje_femenino_mas_bajo["altura"] = float(personaje_femenino_mas_bajo["altura"])
            personaje["altura"] = float(personaje["altura"])
            if (personaje_femenino_mas_bajo["altura"] > personaje["altura"]):
                personaje_femenino_mas_bajo = personaje  

    print("\nNombre = {0} - Altura {1}".format(personaje_femenino_mas_bajo["nombre"],personaje_femenino_mas_bajo["altura"]))   

    print("-------------------------------------\n") 

def calcular_promedio_altura_masculino():
    acumulador_masculino = 0
    contador_masculino = 0
    for personaje in lista_personajes:
        if (personaje["genero"] == "M"):
            acumulador_masculino += float(personaje["altura"])
            contador_masculino += 1

    print("\nPromedio de altura: {0}".format(acumulador_masculino / contador_masculino)) 

    print("-------------------------------------\n") 

def calcular_promedio_altura_femenino():
    acumulador_femenino = 0
    contador_femenino = 0
    for personaje in lista_personajes:
        if (personaje["genero"] == "F"):
            acumulador_femenino += float(personaje["altura"])
            contador_femenino += 1

    print("Promedio de altura: {0}".format(acumulador_femenino / contador_femenino))  

    print("-------------------------------------\n")   

def calcular_cantidad_ojos():
    colores_de_ojos = []
    for color_ojos in lista_personajes:
        colores_de_ojos.append(color_ojos["color_ojos"])

    colores_de_ojos = set(colores_de_ojos)

    lista_colores_ojos = []
    for color in colores_de_ojos:
        dic_color_ojos={"color":color,"cantidad":0}
        for personaje in lista_personajes:
            if (personaje["color_ojos"] == color):
                dic_color_ojos["cantidad"] += 1

        lista_colores_ojos.append(dic_color_ojos)        

    for lista in lista_colores_ojos:
        print("Color: {0} - Cantidad: {1}".format(lista["color"],lista["cantidad"]))
    print("------------------------\n")

def calcular_cantidad_pelo():
    colores_de_pelo = []
    for color_pelo in lista_personajes:
        colores_de_pelo.append(color_pelo["color_pelo"])

    colores_de_pelo = set(colores_de_pelo)

    lista_colores_de_pelo = []
    for color in colores_de_pelo:
        dic_color_pelo={"color":color,"cantidad":0}
        for personaje in lista_personajes:
            if (personaje["color_pelo"] == color):
                dic_color_pelo["cantidad"] += 1

        lista_colores_de_pelo.append(dic_color_pelo)        

    for lista in lista_colores_de_pelo:
        print("Color: {0} - Cantidad: {1}".format(lista["color"],lista["cantidad"]))
    
def calcular_cantidad_inteligencia():
    nivel_inteligencia = []
    for inteligencia in lista_personajes:
        nivel_inteligencia.append(inteligencia["inteligencia"])

    nivel_inteligencia = set(nivel_inteligencia)

    lista_inteligencia = []
    for nivel in nivel_inteligencia:
        dic_inteligencia={"inteligencia":nivel,"cantidad":0}
        for personaje in lista_personajes:
            if (personaje["inteligencia"] == nivel):
                dic_inteligencia["cantidad"] += 1
        lista_inteligencia.append(dic_inteligencia)        
    
    imprimir_lista(lista_inteligencia,"inteligencia")
'''
    for lista in lista_inteligencia:
        if (lista["inteligencia"] == ""):
          lista["inteligencia"] = "No tiene"  
        print("Inteligencia: {0} - Cantidad: {1}".format(lista["inteligencia"],lista["cantidad"]))
'''

def imprimir_lista(lista:list,clave:str):
    for dato in lista:
        if (dato[clave] == ""):
            dato[clave] = "No tiene"  
        print("{2} - {0} - Cantidad: {1}".format(dato[clave],dato["cantidad"],clave))  

def agrupar_heroes_por_ojos():
    grupo_ojos = []
    for personaje in lista_personajes:
        grupo_ojos.append(personaje["color_ojos"])

    grupo_ojos = set(grupo_ojos)

    lista_nombre_por_ojos = []
    for ojos in grupo_ojos:
        dic_ojos = {"ojos":ojos,"heroe":[]}
        for personaje in lista_personajes:
            if (personaje["color_ojos"] == ojos):
                dic_ojos["heroe"].append(personaje["nombre"])
        lista_nombre_por_ojos.append(dic_ojos)                

    for lista in lista_nombre_por_ojos:
        print("Color de ojos: {0} - Heroe: {1}".format(lista["ojos"],lista["heroe"]))

def agrupar_heroes_por_pelo():    
    grupo_pelo = []
    for personaje in lista_personajes:
        grupo_pelo.append(personaje["color_pelo"])

    grupo_pelo = set(grupo_pelo)

    lista_nombre_por_pelo = []
    for pelo in grupo_pelo:
        dic_pelo = {"pelo":pelo,"heroe":[]}
        for personaje in lista_personajes:
            if (personaje["color_pelo"] == pelo):
                dic_pelo["heroe"].append(personaje["nombre"])
        lista_nombre_por_pelo.append(dic_pelo)                

    for lista in lista_nombre_por_pelo:
        if (lista["pelo"] == ""):
            lista["pelo"] = "Sin pelo"
        print("Color de pelo: {0} - Heroe: {1}".format(lista["pelo"],lista["heroe"]))

def agrupar_heroes_por_inteligencia():
    grupo_inteligencia = []
    for personaje in lista_personajes:
        grupo_inteligencia.append(personaje["inteligencia"])

    grupo_inteligencia = set(grupo_inteligencia)

    lista_nombre_por_inteligencia = []
    for nivel in grupo_inteligencia:
        dic_inteligencia = {"nivel":nivel,"heroe":[]}
        for personaje in lista_personajes:
            if (personaje["inteligencia"] == nivel):
                dic_inteligencia["heroe"].append(personaje["nombre"])
        lista_nombre_por_inteligencia.append(dic_inteligencia)                

    for lista in lista_nombre_por_inteligencia:
        if (lista["nivel"] == ""):
            lista["nivel"] = "No tiene"
        print("Inteligencia: {0} - Heroe: {1}".format(lista["nivel"],lista["heroe"]))

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
while(True):
    opcion = input("\nElija una opcion: \n"
                   " 1 = Lista de Heroes  \n"
                   " 2 = Lista de Heroinas \n"
                   " 3 = Heroe mas alto\n"
                   " 4 = Heroina mas alta\n"
                   " 5 = Heroe mas bajo\n"
                   " 6 = Heroina mas baja\n"
                   " 7 = Promedio de altura masculino\n"
                   " 8 = Promedio de altura femenino\n"
                   " 9 = Cantidad color de ojos\n"
                   "10 = Cantidad color de pelo\n"
                   "11 = Cantidad nivel de inteligencia\n"
                   "12 = Grupo de Heroes por color de ojos\n"
                   "13 = Grupo de Heroes por color de pelo\n"
                   "14 = Grupo de Heroes por tipo de inteligencia\n"
                   "15 = Salir del programa\n\n> ")

    if (opcion == "1"):
        calcular_nombre_heroes()
    elif (opcion == "2"):
        calcular_nombre_heroinas()
    elif (opcion == "3"):
        calcular_heroe_mas_alto()
    elif (opcion == "4"):
        calcular_heroina_mas_alta()
    elif (opcion == "5"):
        calcular_heroe_mas_bajo() 
    elif (opcion == "6"):
        calcular_heroina_mas_bajo() 
    elif (opcion == "7"):
        calcular_promedio_altura_masculino()
    elif (opcion == "8"):
        calcular_promedio_altura_femenino()
    elif (opcion == "9"):
        calcular_cantidad_ojos()
    elif (opcion == "10"):
        calcular_cantidad_pelo()
    elif (opcion == "11"):
        calcular_cantidad_inteligencia()
    elif (opcion == "12"):
        agrupar_heroes_por_ojos()
    elif (opcion == "13"):
        agrupar_heroes_por_pelo()
    elif (opcion == "14"):
        agrupar_heroes_por_inteligencia()                                                    
    elif (opcion == "15"):
        break




