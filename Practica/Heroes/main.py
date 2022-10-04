import io
from funciones import *

def heroes_app():
    lista_heroes = importar_archivo("Practica\Heroes\data_stark.json")
    while(True):
        opcion = menu_principal()
        if (opcion == "1"):
            cantidad = int(validar_dato_general("Ingrese la cantidad: ","^[0-9]+$"))
            if (cantidad == -1 or cantidad > len(lista_heroes)):
                print("Error: Ingrese la cantidad correctamente")
                continue
            lista = mostrar_heroes(lista_heroes,cantidad)
            print(lista)
        elif(opcion == "2"):
            orden = validar_dato_general("Ingrese el orden: ","^asc|desc$")
            if (orden == -1):
                print("Error: Ingrese el orden correctamente")
                continue
            lista = ordenar_lista(lista_heroes,"altura",orden)
            print(lista)
        elif(opcion == "3"):
            orden = validar_dato_general("Ingrese el orden: ","^asc|desc$")
            if (orden == -1):
                print("Error: Ingrese el orden correctamente")
                continue
            lista = ordenar_lista(lista_heroes,"peso",orden)
            print(lista)
        elif(opcion == "4"):
            pass
        elif(opcion == "5"):
            pass
        elif(opcion == "6"):
            pass
        elif(opcion == "7"):
            break
        
heroes_app()