from funciones import *

Lista_personajes = leer_archivo("Clase_10\Ejercicio12\data_stark.json")

def heroes_app(lista_heroes:list):
    while(True):
        opcion = menu_principal()
        if (opcion == "1"):
            cantidad = input("Ingrese la cantidad: ")
            cantidad = int(validar_respuesta(cantidad,"[0-9]+"))
            if (cantidad == -1):
                print("Error: Ingrese un numero entero")
                continue
            lista = mostrar_heroes(lista_heroes,cantidad)
            mensaje = convertir_lista_str_formateado(lista,"identidad")
            print(mensaje)
        elif(opcion == "2"):
            orden = input("Lista en forma ascendente 'asc' o descendente 'desc'? ")
            orden = orden.lower()
            orden = validar_respuesta(orden,"^asc|desc$")
            if (orden == -1):
                print("Error, Ingrese 'asc' o 'desc'")
                continue
            lista_altura = ordenar_dato(lista_heroes,"altura",orden)
            mensaje = convertir_lista_str_formateado(lista_altura,"altura")
            print(mensaje)
        elif(opcion == "3"):
            orden = input("Quiere ordenar la lista de manera ascendente (asc) o descendente (desc)? ")
            orden = orden.lower()
            orden = validar_respuesta(orden,"^asc|desc$")
            if (orden == -1):
                print("Error, Ingrese 'asc' o 'desc'")
                continue
            lista_fuerza = ordenar_dato(lista_heroes,"fuerza",orden)
            mensaje = convertir_lista_str_formateado(lista_fuerza,"fuerza")
            print(mensaje)
        elif(opcion == "4"):
            tipo = input("Filtrar menores o mayores (menor/mayor)? ")
            tipo = tipo.lower()
            tipo = validar_respuesta(tipo,"^menor|mayor$")
            key = input("Ingrese una key del tipo numerico: ")
            key = validar_respuesta(key,"^altura|peso|fuerza$")
            if(tipo == -1):
                print("Error: Tipo invalido, Ingrese menor o mayor")
                continue
            if(key == -1):
                print("Error: La key no es numerica")    
                continue
            lista_filtro = filtrar_por_dato(lista_heroes,key,tipo)
            mensaje = convertir_lista_str_formateado(lista_filtro,key)
            print(mensaje)
        elif(opcion == "5"):
            tipo = input("Ingrese que tipo de inteligencia quiere buscar (good,average,high): ")
            tipo = tipo.lower()
            tipo = validar_respuesta(tipo,"^good|average|high$")
            if(tipo == -1):
                print("Error: Tipo invalido, Ingrese alguna de las opciones correctas")
                continue
            buscar_e_imprimir_heroe_tipo(lista_heroes,"inteligencia",tipo)
        elif(opcion == "6"):
            exportar_csv(mensaje)
        elif(opcion == "7"):
            break

heroes_app(Lista_personajes)
