#--------------------- Punto A -------------------------------
def imprimir_lista(lista:list):
    print(lista)

#--------------------- Punto B -------------------------------
def mostrar_nombre_heroes(lista:list):
    for personaje in lista:
        print(personaje["nombre"])

#--------------------- Punto C -------------------------------
#---Recorriendo nombres con altura en la lista---
def mostrar_nombre_mas_altura(lista:list):
    for personaje in lista:
        print("{0} - {1}".format(personaje["nombre"], personaje["altura"]))

#--------------------- Punto D -------------------------------
def calcular_mas_alto(lista:list):
    #---Personaje con mas altura----
    superheroe_mas_alto = lista[0]
    for personaje in lista:
        superheroe_float = float(superheroe_mas_alto["altura"])
        personaje_float = float(personaje["altura"])
        if (superheroe_float < personaje_float):
            superheroe_mas_alto = personaje

    print("Personaje mas alto: {0}\nAltura: {1} cm".format(superheroe_mas_alto["nombre"],superheroe_mas_alto["altura"]))
    #------------------------------

#--------------------- Punto E -------------------------------
def calcular_mas_bajo(lista:list):
    #---Personaje con menos altura----
    superheroe_mas_bajo = lista[0]
    for personaje in lista:
        superheroe_float = float(superheroe_mas_bajo["altura"])
        personaje_float = float(personaje["altura"])
        if (superheroe_float > personaje_float):
            superheroe_mas_bajo = personaje

    print("Personaje mas bajo: {0}\nAltura: {1} cm".format(superheroe_mas_bajo["nombre"],superheroe_mas_bajo["altura"]))   
    #--------------------------------

#--------------------- Punto F -------------------------------
def calcular_promedio_altura(lista:list):
    #---Promedio de altura----
    acumulador_altura = 0
    contador_altura = 0
    for personaje in lista:
        personaje_float = float(personaje["altura"])
        acumulador_altura += personaje_float
        contador_altura += 1
    
    print(f"Promedio de altura: {acumulador_altura / contador_altura}")
    #---------------------------

#--------------------- Punto H -------------------------------

#H.1
def calcular_mas_pesado(lista:list):
    #----Superheroe mas pesado----
    superheroe_mas_pesado = lista[0]
    for personaje in lista:
        superheroe_float = float(superheroe_mas_pesado["peso"])
        personaje_float = float(personaje["peso"])
        if (superheroe_float < personaje_float):
            superheroe_mas_pesado = personaje

    print("Personaje mas pesado: {0}\nPeso: {1} kg".format(superheroe_mas_pesado["nombre"],superheroe_mas_pesado["peso"])) 
    #--------------------------------

#H.2
def calcular_mas_liviano(lista:list):
    #----Superheroe mas liviano----
    superheroe_menos_pesado = lista[0]
    for personaje in lista:
        superheroe_float = float(superheroe_menos_pesado["peso"])
        personaje_float = float(personaje["peso"])
        if (superheroe_float > personaje_float):
            superheroe_menos_pesado = personaje

    print("Personaje mas liviano: {0}\nPeso: {1} kg".format(superheroe_menos_pesado["nombre"],superheroe_menos_pesado["peso"])) 