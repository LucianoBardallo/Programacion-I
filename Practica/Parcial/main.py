from funciones import *

def pokemones_app():
    lista_pokemones = importar_archivo("Practica\Parcial\pokedex.json")
    lista_pokemones = normalizar_datos(lista_pokemones)
    mensaje = ""
    while(True):
        opcion = menu_principal()
        if (opcion == "1"):
            cantidad = int(validar_dato_general("Ingrese la cantidad: ","^[0-9]+$"))
            if (cantidad == -1 or cantidad > len(lista_pokemones)):
                print("Error: Ingrese la cantidad correctamente")
                continue
            lista = mostrar_pokemones(lista_pokemones,cantidad)
            mensaje = formatear_lista(lista)
            print(mensaje)
        elif (opcion == "2"):
            orden = validar_dato_general("Ingrese el orden (ascende(asc) o descendente(desc)): ","^asc|desc$")
            if (orden == -1):
                print("Ingrese el orden correctamente")
                continue
            lista = ordenar_lista(lista_pokemones,"poder",orden)
            mensaje = formatear_lista(lista)
            print(mensaje)
        elif (opcion == "3"):
            orden = validar_dato_general("Ingrese el orden (ascende(asc) o descendente(desc)): ","^asc|desc$")
            if (orden == -1):
                print("Ingrese el orden correctamente")
                continue
            lista = ordenar_lista(lista_pokemones,"id",orden)
            mensaje = formatear_lista(lista)
            print(mensaje)
        elif (opcion == "4"):
            key = validar_dato_general("Ingrese una clave (evoluciones,tipo,fortaleza,debilidad): ","^evoluciones|tipo|fortaleza|debilidad$")
            if (key == -1):
                print("Ingrese la key correctamente")
                continue
            tipo = validar_dato_general("Ingrese el tipo a mostrar la lista, menor o mayor: ", "^menor|mayor$")
            if (tipo == -1):
                print("Ingrese el tipo correctamente")
                continue
            lista = filtrar_pokemon_por_promedio(lista_pokemones,key,tipo)
            mensaje = formatear_lista(lista)
            print(mensaje)
        elif (opcion == "5"):
            tipo = validar_dato_general("Ingrese tipo (planta,agua,fuego,volador,electrico,fantasma,veneno,hielo,psiquico,lucha,acero): ","^planta|agua|fuego|volador|electrico|fantasma|veneno|hielo|psiquico|lucha|acero$")
            if (tipo == -1):
                print("Ingrese el tipo correctamente")
                continue
            lista = buscar_pokemon_dato(lista_pokemones,"tipo",tipo)
            mensaje = formatear_lista(lista)
            print(mensaje)
        elif (opcion == "6"):
            if mensaje != "":
                exportar_archivo(mensaje)
            else:
                print("No hay nada que exportar")
        elif (opcion == "7"):
            print("Gracias por usar nuestro programa")
            break

pokemones_app()