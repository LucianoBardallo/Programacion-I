from data_stark import lista_personajes
from funciones import *

stark_normalizar_datos(lista_personajes)

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
