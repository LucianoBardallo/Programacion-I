from funciones import *

def pokemones_app():
    lista_pokemones = importar_archivo("Practica\Parcial_2\pokedex.json")
    lista = ""
    while(True):
        imprimir_menu()
        opcion = obtener_opcion_principal("Ingrese una opcion: ")
        if (opcion == "1"):
            cantidad = int(validar_dato_general("Ingrese la cantidad: ","^[0-9]+"))
            if (cantidad == -1 or cantidad > len(lista_pokemones)):
                print("Error: Ingrese cantidad correctamente")
                continue
            lista = mostrar_pokemones(lista_pokemones,cantidad)
            lista = formatear_lista(lista)
            print(lista)
        elif(opcion == "2"):
            orden = validar_dato_general("Ingrese el orden a mostrar la lista: ", "^asc|desc$")
            if (orden == -1):
                print("Error: Ingrese el orden correctamente")
                continue
            lista = ordenar_lista(lista_pokemones,"poder",orden)
            lista = formatear_lista(lista)
            print(lista)
        elif(opcion == "3"):
            orden = validar_dato_general("Ingrese el orden a mostrar la lista: ", "^asc|desc$")
            if (orden == -1):
                print("Error: Ingrese el orden correctamente")
                continue
            lista = ordenar_lista(lista_pokemones,"id",orden)
            lista = formatear_lista(lista)
            print(lista)
        elif(opcion == "4"):
            key = validar_dato_general("Ingrese cualquiera de estas claves (evoluciones|tipo|fortaleza|debilidad): ","^evoluciones|tipo|fortaleza|debilidad$")
            if (key == -1):
                print("Error: Ingrese la key correctamente")
                continue
            tipo = validar_dato_general("Ingrese menor o mayor: ", "^menor|mayor$")
            if (tipo == -1):
                print("Error: Ingrese el tipo correctamente")
                continue
            lista = filtrar_lista_por_promedio(lista_pokemones,key,tipo)
            lista = formatear_lista(lista)
            print(lista)
        elif(opcion == "5"):
            tipo = validar_dato_general("Ingrese el tipo de pokemon: ", "^planta|fuego|electrico|volador|agua|fantasma|veneno|psiquico|lucha|acero|hielo$")
            if (tipo == -1):
                print("Error: Ingrese el tipo correctamente")
                continue
            lista = buscar_heroe_por_tipo(lista_pokemones,tipo)
            lista = formatear_lista(lista)
            print(lista)
        elif(opcion == "6"):
            if(lista != ""):
                exportar_archivo(lista)
            else:
                print("Error: Eliga primero alguna de las opciones")
        elif(opcion == "7"):
            break

pokemones_app()