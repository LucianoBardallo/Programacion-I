from data_stark import lista_heroes
from funciones import *

def stark_menu_principal(lista_heroes:list):
    while(True):
        opcion = obtener_valor_opcion()

        if (opcion == "A"):
            calcular_nombre_heroes(lista_heroes)
        elif (opcion == "B"):
            calcular_nombre_heroinas(lista_heroes)
        elif (opcion == "C"):
            calcular_heroe_mas_alto(lista_heroes)
        elif (opcion == "D"):
            calcular_heroina_mas_alta(lista_heroes)
        elif (opcion == "E"):
            calcular_heroe_mas_bajo(lista_heroes) 
        elif (opcion == "F"):
            calcular_heroina_mas_bajo(lista_heroes) 
        elif (opcion == "G"):
            calcular_promedio_altura_masculino(lista_heroes)
        elif (opcion == "H"):
            calcular_promedio_altura_femenino(lista_heroes)
        elif (opcion == "I"):
            calcular_cantidad_ojos(lista_heroes)
        elif (opcion == "J"):
            calcular_cantidad_pelo(lista_heroes)
        elif (opcion == "K"):
            calcular_cantidad_inteligencia(lista_heroes)
        elif (opcion == "L"):
            agrupar_heroes_por_ojos(lista_heroes)
        elif (opcion == "M"):
            agrupar_heroes_por_pelo(lista_heroes)
        elif (opcion == "N"):
            agrupar_heroes_por_inteligencia(lista_heroes)                                                    
        elif (opcion == "Z"):
            break


stark_menu_principal(lista_heroes)

