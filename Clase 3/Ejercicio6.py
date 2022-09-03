from data_stark import lista_personajes

def calcular_mas_alto():
    #---Personaje con mas altura----
    superheroe_mas_alto = lista_personajes[0]
    for personaje in lista_personajes:
        superheroe_float = float(superheroe_mas_alto["altura"])
        personaje_float = float(personaje["altura"])
        if (superheroe_float < personaje_float):
            superheroe_mas_alto = personaje

    print("Personaje mas alto: {0}\nAltura: {1} cm".format(superheroe_mas_alto["nombre"],superheroe_mas_alto["altura"]))
    #------------------------------

def calcular_mas_bajo():
    #---Personaje con menos altura----
    superheroe_mas_bajo = lista_personajes[0]
    for personaje in lista_personajes:
        superheroe_float = float(superheroe_mas_bajo["altura"])
        personaje_float = float(personaje["altura"])
        if (superheroe_float > personaje_float):
            superheroe_mas_bajo = personaje

    print("Personaje mas bajo: {0}\nAltura: {1} cm".format(superheroe_mas_bajo["nombre"],superheroe_mas_bajo["altura"]))   
    #--------------------------------

def calcular_promedio_altura():
    #---Promedio de altura----
    acumulador_altura = 0
    contador_altura = 0
    for personaje in lista_personajes:
        personaje_float = float(personaje["altura"])
        acumulador_altura += personaje_float
        contador_altura += 1
    
    print(f"Promedio de altura: {acumulador_altura / contador_altura}")
    #---------------------------

def calcular_mas_pesado():
    #----Superheroe mas pesado----
    superheroe_mas_pesado = lista_personajes[0]
    for personaje in lista_personajes:
        superheroe_float = float(superheroe_mas_pesado["peso"])
        personaje_float = float(personaje["peso"])
        if (superheroe_float < personaje_float):
            superheroe_mas_pesado = personaje

    print("Personaje mas pesado: {0}\nPeso: {1} kg".format(superheroe_mas_pesado["nombre"],superheroe_mas_pesado["peso"])) 
    #--------------------------------

def calcular_mas_liviano():
    #----Superheroe mas liviano----
    superheroe_menos_pesado = lista_personajes[0]
    for personaje in lista_personajes:
        superheroe_float = float(superheroe_menos_pesado["peso"])
        personaje_float = float(personaje["peso"])
        if (superheroe_float > personaje_float):
            superheroe_menos_pesado = personaje

    print("Personaje mas liviano: {0}\nPeso: {1} kg".format(superheroe_menos_pesado["nombre"],superheroe_menos_pesado["peso"])) 
    #-------------------------------

'''
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


#----Recorriendo nombres de la lista-----
for personaje in lista_personajes:
    print(personaje["nombre"])


#---Recorriendo nombres con altura en la lista---
for personaje in lista_personajes:
    print(personaje["nombre"], personaje["altura"])

#----Nombre personaje con mas y menos altura----
print("Personaje mas alto: {0} \nPersonaje mas bajo: {1}".format(superheroe_mas_alto["nombre"], superheroe_mas_bajo["nombre"]))

'''

while(True):
    opcion = input("\nElija una opcion: \n1 = Personaje mas alto \n2 = Personaje mas bajo\n3 = Persoje mas pesado\n4 = Personaje mas liviano\n5 = Promedio de altura\n6 = Salir\n\n>")

    if (opcion == "1"):
        calcular_mas_alto()
    elif (opcion == "2"):
        calcular_mas_bajo()
    elif (opcion == "3"):
        calcular_mas_pesado()
    elif (opcion == "4"):
        calcular_mas_liviano()
    elif (opcion == "5"):
        calcular_promedio_altura()
    elif (opcion == "6"):
        break














