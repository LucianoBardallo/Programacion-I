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
    opcion = input("Elija una opcion: \n1 = Lista de Heroes  \n2 = Lista de Heroinas \n3 = Heroe mas alto\n4 = Heroina mas alta\n5 = Heroe mas bajo\n6 = Heroina mas baja\n7 = Promedio de altura masculino\n8 = Promedio de altura femenino\n\n> ")

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
        pass                           
    elif (opcion == "10"):
        break
 
 
'''
contador_brown = 0
contador_green = 0
contador_blue = 0
contador_yellow = 0
contador_yellow_iris = 0
contador_hazel = 0
contador_red = 0
contador_silver = 0

for personaje in lista_personajes:
    if (personaje["color_ojos"] == "Brown"):
        contador_brown += 1
    elif (personaje["color_ojos"] == "Green"):
        contador_green += 1
    elif (personaje["color_ojos"] == "Blue"):
        contador_blue += 1
    elif (personaje["color_ojos"] == "Yellow"):
        contador_yellow += 1
    elif (personaje["color_ojos"] == "Yellow (without irises)"):
        contador_yellow_iris += 1
    elif (personaje["color_ojos"] == "Hazel"):
        contador_hazel += 1
    elif (personaje["color_ojos"] == "Red"):
        contador_red += 1
    elif (personaje["color_ojos"] == "Silver"):
        contador_silver += 1    

for personaje in lista_personajes:
    if (personaje["color_pelo"] == "Brown"):
        contador_brown += 1
    elif (personaje["color_pelo"] == "Green"):
        contador_green += 1
    elif (personaje["color_pelo"] == "Black"):
        contador_blue += 1
    elif (personaje["color_pelo"] == "Yellow"):
        contador_yellow += 1
    elif (personaje["color_pelo"] == "Red / Orange"):
        contador_yellow_iris += 1
    elif (personaje["color_pelo"] == "Blond"):
        contador_hazel += 1
    elif (personaje["color_pelo"] == "White"):
        contador_red += 1
    elif (personaje["color_pelo"] == "Silver"):
        contador_silver += 1  

'''


