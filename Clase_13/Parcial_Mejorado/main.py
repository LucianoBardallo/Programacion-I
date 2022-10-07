'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones

def starwars_app():
    lista_personajes = funciones.cargar_json("Clase_13\Parcial_Mejorado\data.json")
    lista_personajes = funciones.normalizar_datos(lista_personajes)
    mensaje = funciones.formatear_mensaje(lista_personajes)
    while(True):
        print("\n1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input("Ingrese una opcion: ")
        if(respuesta=="1"):
            lista = lista_personajes[:]
            lista.sort(key = lambda personaje: personaje["height"], reverse = True)
            funciones.mostrar_heroes(lista)
        elif(respuesta=="2"):
            lista = funciones.calcular_genero_mas_alto(lista_personajes,"height")
            funciones.mostrar_heroes(lista)
        elif(respuesta=="3"):
            lista = lista_personajes[:]
            lista.sort(key = lambda personaje: personaje["mass"], reverse = True)
            funciones.mostrar_heroes(lista)
        elif(respuesta=="4"):
            lista = funciones.buscar_heroe(lista_personajes)
            funciones.mostrar_heroes(lista)  
        elif(respuesta=="5"):
            funciones.exportar_archivo(mensaje)
        elif(respuesta=="6"):
            print("Que la fuerza te acompañe!")
            break


starwars_app()

