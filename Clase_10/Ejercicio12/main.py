from funciones import *

Lista_personajes = importar_archivo("Repaso\Heroes\data_stark.json")

def heroes_app(lista_heroes:list):
    while(True):
        opcion = menu_principal()
        if(opcion == "1"):
            cantidad = input("Ingrese cantidad: ")
            cantidad = int(validar_respuesta_general(cantidad,"[0-9]+"))
            if (cantidad == -1):
                print("Error: Ingrese un numero entero")
                continue
            lista = mostrar_heroes(lista_heroes,cantidad)
            mensaje = mostrar_heroe_formateado(lista)
            print(mensaje)
        elif(opcion == "2"):
            orden = input("Ingrese el orden (asc/desc)")
            orden = validar_respuesta_general(orden,"^asc|desc$")
            if (orden == -1):
                print("Error: Ingrese 'asc' o 'desc'")
                continue
            lista = ordenar_lista(lista_heroes,"altura",orden)
            mensaje = mostrar_heroe_formateado(lista)
            print(mensaje)
        elif(opcion == "3"):
            orden = input("Ingrese el orden (asc/desc): ")
            orden = validar_respuesta_general(orden,"^asc|desc$")
            if (orden == -1):
                print("Error: Ingrese 'asc' o 'desc'")
                continue
            lista = ordenar_lista(lista_heroes,"fuerza",orden)
            mensaje = mostrar_heroe_formateado(lista)
            print(mensaje)
        elif(opcion == "4"):
            key = input("Ingrese la clave a promediar: ")
            key = validar_respuesta_general(key,"^altura|peso|fuerza$")
            tipo = input("Ingrese menor o mayor: ")
            tipo = tipo.lower()
            tipo = validar_respuesta_general(tipo,"^menor|mayor$")
            if(tipo == -1):
                print("Error: Tipo invalido, Ingrese menor o mayor")
                continue
            if(key == -1):
                print("Error: La key no es numerica")    
                continue
            lista = filtrar_heroes_por_dato(lista_heroes,key,tipo)
            mensaje = mostrar_heroe_formateado(lista)
            print(mensaje)
        elif(opcion == "5"):
            tipo = input("Ingrese good/average/high: ")
            tipo = tipo.lower()
            tipo = validar_respuesta_general(tipo,"^good|average|high$")
            buscar_e_imprimir_heroe_tipo(lista_heroes,"inteligencia",tipo)
        elif(opcion == "6"):
            try:
                exportar_csv(mensaje)
            except:
                print("Primero ingrese alguna de estas opciones (1-4)")
                continue
        elif(opcion == "7"):
            break
    
heroes_app(Lista_personajes)