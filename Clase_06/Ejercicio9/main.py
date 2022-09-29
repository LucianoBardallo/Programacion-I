from data_stark import lista_personajes
from funciones import *

#6.3
def stark_marvel_app_3(lista_heroes:list):
  '''
  Es función se encarga de la ejecución principal del programa. 
  '''
  while True:
    opcion = stark_menu_principal()
    try:
      if (opcion == "S"):
        break
      elif (int(opcion) == 1):
        stark_imprimir_nombres_con_iniciales(lista_heroes)
      elif (int(opcion) == 2):
        stark_generar_codigos_heroes(lista_heroes)
      elif (int(opcion) == 3):
        stark_normalizar_datos(lista_heroes)
      elif (int(opcion) == 4):
        stark_imprimir_indice_nombre(lista_heroes)
      elif (int(opcion) == 5):
        stark_navegar_fichas(lista_heroes)
    except:
      continue

stark_marvel_app_3(lista_personajes)


