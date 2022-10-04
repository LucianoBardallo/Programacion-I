from funciones import *



def heroes_app():
    lista_heroes = importar_archivo("Repaso\Heroes\data_stark.json")
    lista_heroes = normalizar_datos(lista_heroes)
    lista = ""
    while(True):
        opcion = menu_principal()
        if(opcion == "1"):
            cantidad = int(validar_dato_general("Ingrese cantidad: ","[0-9]+"))
            if(cantidad == -1 or cantidad > len(lista_heroes)):
                print("Error: La cantidad no es correcta")
                continue   
            lista = mostrar_heroes(lista_heroes,cantidad)
            lista = mostrar_heroe_formateado(lista)
            print(lista)
        elif(opcion == "2"):
            orden = validar_dato_general("Ingrese el orden (asc/desc): ","^asc|desc$")
            if(orden == -1):
                print("Error: El orden no es correcto")
                continue   
            lista = ordenar_lista(lista_heroes,"altura",orden)
            lista = mostrar_heroe_formateado(lista)
            print(lista)
        elif(opcion == "3"):
            orden = validar_dato_general("Ingrese el orden (asc/desc): ","^asc|desc$")
            if(orden == -1):
                print("Error: El orden no es correcto")
                continue   
            lista = ordenar_lista(lista_heroes,"fuerza",orden)
            lista = mostrar_heroe_formateado(lista)
            print(lista)
        elif(opcion == "4"):
            key = validar_dato_general("Ingrese la clave a promediar: ","^altura|peso|fuerza$")
            if(key == -1):
                print("Error: La key no es numerica")
                continue   
            tipo = validar_dato_general("Ingrese menor o mayor: ","^menor|mayor$")
            if(tipo == -1):
                print("Error: Tipo invalido")
                continue
            lista = filtrar_heroes_por_dato(lista_heroes,key,tipo)
            lista = mostrar_heroe_formateado(lista)
            print(lista)
        elif(opcion == "5"):
            tipo = validar_dato_general("Ingrese good/average/high: ","^good|average|high$")
            if (tipo == -1):
                print("Error: Tipo invalido")
                continue
            lista = buscar_heroe_tipo(lista_heroes,"inteligencia",tipo)
            lista = mostrar_heroe_formateado(lista)
            print(lista)
        elif(opcion == "6" and len(lista) > 0):
            exportar_csv(lista)
        elif(opcion == "7"):
            break
    
heroes_app()