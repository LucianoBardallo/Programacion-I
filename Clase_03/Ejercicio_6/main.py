from data_stark import lista_personajes

from funciones import *

#--------------------- MENU -------------------------------
def menu_app():
    while(True):
        opcion = input("\n--------MENU--------- \n"
                        "A = Mostrar Lista \n"
                        "B = Nombre de heroes\n"
                        "C = Nombre de heroes con su altura\n"
                        "D = Personaje mas alto \n"
                        "E = Personaje mas bajo\n"
                        "F = Promedio de altura\n"
                        "G = Personaje mas liviano\n"
                        "H = Persoje mas pesado\n"
                        "Z = Salir\n"
                        "---------------------\n\n"
                        "Ingrese una opcion: ")

        if (opcion == "A"):
            imprimir_lista(lista_personajes)
        elif (opcion == "B"):
            mostrar_nombre_heroes(lista_personajes)
        elif (opcion == "C"):
            mostrar_nombre_mas_altura(lista_personajes)
        elif (opcion == "D"):
            calcular_mas_alto(lista_personajes)
        elif (opcion == "E"):
            calcular_mas_bajo(lista_personajes)
        elif (opcion == "F"):
            calcular_promedio_altura(lista_personajes)
        elif (opcion == "G"):
            calcular_mas_liviano(lista_personajes)
        elif (opcion == "H"):
            calcular_mas_pesado(lista_personajes)
        elif (opcion == "Z"):
            break
    
menu_app()














