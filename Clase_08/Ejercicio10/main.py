from funciones import *

lista_personajes = leer_archivo("Clase_08\Ejercicio10\data_stark.json")
stark_normalizar_datos(lista_personajes)

#1.3
def stark_marvel_app_5(lista_heroes:list):
    while(True):
        opcion = stark_menu_principal_desafio_5()
        if (opcion == "A"):
            stark_guardar_heroe_genero(lista_heroes,"m")
        elif (opcion == "B"):
            stark_guardar_heroe_genero(lista_heroes,"f")
        elif (opcion == "C"):
            stark_calcular_imprimir_guardar_heroe_genero(lista_heroes,"altura","M","maximo")
        elif (opcion == "D"):
            stark_calcular_imprimir_guardar_heroe_genero(lista_heroes,"altura","F","maximo")
        elif (opcion == "E"):
            stark_calcular_imprimir_guardar_heroe_genero(lista_heroes,"altura","M","minimo") 
        elif (opcion == "F"):
            stark_calcular_imprimir_guardar_heroe_genero(lista_heroes,"altura","F","minimo")
        elif (opcion == "G"):
            stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes,"M")
        elif (opcion == "H"):
            stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes,"F")
        elif (opcion == "I"):
            stark_calcular_imprimir_guardar_heroe_genero(lista_heroes,"altura","M","maximo")
            stark_calcular_imprimir_guardar_heroe_genero(lista_heroes,"altura","F","maximo")
            stark_calcular_imprimir_guardar_heroe_genero(lista_heroes,"altura","M","minimo")
            stark_calcular_imprimir_guardar_heroe_genero(lista_heroes,"altura","F","minimo") 
        elif (opcion == "J"):
            stark_calcular_cantidad_por_tipo(lista_heroes,"color_ojos")
        elif (opcion == "K"):
            stark_calcular_cantidad_por_tipo(lista_heroes,"color_pelo")
        elif (opcion == "L"):
            stark_calcular_cantidad_por_tipo(lista_heroes,"inteligencia")
        elif (opcion == "M"):
            stark_listar_heroes_por_dato(lista_heroes,"color_ojos")
        elif (opcion == "N"):
            stark_listar_heroes_por_dato(lista_heroes,"color_pelo")
        elif (opcion == "O"):
            stark_listar_heroes_por_dato(lista_heroes,"inteligencia")                                                    
        elif (opcion == "Z"):
            break

stark_marvel_app_5(lista_personajes)



