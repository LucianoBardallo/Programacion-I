import re

#---------------------PUNTO 1----------------

#1.1
def extraer_iniciales(nombre_heroe:str):
  '''
  Esta funcion se encarga de extraer las inicianes de un string separada por puntos.

  Parametros: Recibe un string representando el nombre de un heroe

  Retorna: "N/A" en caso de que el string este vacio
  '''
  retorno = "N/A"
  if (len(nombre_heroe) > 0):
    nombre_heroe = nombre_heroe.replace(" the "," ")
    nombre_heroe = nombre_heroe.replace("-"," ")
    nombre_heroe = nombre_heroe.split(" ")

    iniciales = ""
    for nombre in nombre_heroe:
      iniciales += nombre[0] + "."
     
    retorno = iniciales
    
  return retorno

#1.2
def definir_iniciales_nombre(heroe:dict)->bool:
  '''
  Esta funcion se encarga de agregar las iniciales de los heroes a un diccionario como nueva clave

  Parametros: Recibe un diccionario representando a los datos de un heroe

  Retorna: True en caso de que todo salga bien, False en caso contrario
  '''
  retorno = False 
  if (type(heroe) == type(dict()) and len(heroe["nombre"]) > 0):
    iniciales = extraer_iniciales(heroe["nombre"])
    heroe["iniciales"] = iniciales
    retorno = True
  
  return retorno

#1.3
def agregar_iniciales_nombre(lista_heroes:list) -> bool:
  '''
  Esta funcion se encarga de iterar la lista y agregarle las iniciales donde corresponda

  Parametros: Recibe una lista representando a todos los heroes

  Retorna: True en caso de haber finalizado con éxito o False en caso de que haya ocurrido un error
  '''
  for heroe in lista_heroes:
    retorno = "Error lista no es del tipo list o esta vacia"
    if (type(lista_heroes) == type([]) and len(lista_heroes) > 0):
      validar = definir_iniciales_nombre(heroe)
      if (validar == True):
        retorno = True
      elif (validar == False):
        print("El origen de datos no contiene el formato correcto")
        retorno = False
        break 

  return retorno


#1.3
def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
  '''
  Esta funcion se encarga de tomar el nombre del heroe con sus iniciales y 
  mostrarlos en pantalla con el formato "Iron Man (I.M.)"

  Parametros: Recibe una lista reprensentado a todos los heroes
  '''
  if (type(lista_heroes) == type([]) and len(lista_heroes) > 0):
    agregar_iniciales_nombre(lista_heroes)
    for heroe in lista_heroes:
      agregar_iniciales_nombre(heroe)
      print("*{0} - ({1})".format(heroe["nombre"],heroe["iniciales"]))

#---------------------PUNTO 2----------------

#2.1
def generar_codigo_heroe(id_heroe:int,genero_heroe:str) -> str:
  '''
Esta funcion se encarga de generar un codigo para los heroes con maximo 10 caracteres con el formato "F-00000001"

Parametros: Recibe un id de heroe del tipo entero, y el genero del heroe.

Retorna: El codigo generado de tipo string
'''
  if (type(id_heroe) == type(int()) and len(genero_heroe) > 0 and (genero_heroe == "F" or genero_heroe == "M" or genero_heroe == "NB")):
    id_heroe = str(id_heroe)
    if (genero_heroe == "NB"):
      id_heroe = id_heroe.zfill(7) 
    else:
      id_heroe = id_heroe.zfill(8)  
    codigo_heroe = "{0}-{1}".format(genero_heroe,id_heroe)
    return codigo_heroe

#2.2
def agregar_codigo_heroe(heroe:dict)->bool:
  '''
  Esta funcion se encarga de generar un codigo y agregarlo al diccionario como una clave nueva

  Parametros: Recibe un diccionario representando a los datos de un heroe

  Retorna: True si todo sale bien, False en caso contrario
  '''
  retorno = False
  if (len(heroe) > 0):
    codigo_heroe = generar_codigo_heroe(heroe["posicion"],heroe["genero"])
    if(len(codigo_heroe) == 10):
      heroe["codigo"] = codigo_heroe
      retorno = True
  return retorno

#2.3
def stark_generar_codigos_heroes(lista_heroes:list):
  '''
  Esta funcion se encarga de iterar una lista de heroes y agregarles el codigo a cada uno,
  despues imprime en pantalla cuantos codigos se asignaron y cual fue el primer y el ultimo codigo 

  Parametros: Recibe una lista que representa a todos los heroes
  '''
  if (len(lista_heroes) > 0):
    i = 0
    for heroe in lista_heroes:
      if (type(heroe) == type({}) and len(heroe["genero"]) > 0):
        i += 1
        heroe["posicion"] = i
        agregar_codigo_heroe(heroe)
      
    print("Se asignaron {0} codigos"
          "\nEl código del primer heroe es: {1}"
          "\nEl código del ultimo heroe es: {2}".format(heroe["posicion"],lista_heroes[0]["codigo"],lista_heroes[-1]["codigo"]))
  else:
    print("El origen de datos no contiene el formato correcto")
   
#---------------------PUNTO 3----------------

#3.1
def sanitizar_entero(numero_str:str) -> int:
  '''
  Esta función se encarga de analizar el string recibido y determinar si se puede transformar a un numero flotante

  Parametros: Recibe un string

  Retorna: El numero si es valido, -1 en caso de contiene caracteres no numericos, -2 en caso de ser negativo, 
  y -3 en caso de que no sea ninguno de los casos anteriores
  '''
  numero_str = numero_str.strip()
  try:
    try:
      numero_int = int(numero_str)
      if (numero_int < 0):
        retorno = -2
      else:
        retorno = numero_int
    except:
      validacion = numero_str.isalnum()
      if (validacion == True):
        retorno = -1
    return retorno
  except:
      return -3  

#3.2
def sanitizar_flotante(numero_str:str) -> float:
  '''
  Esta funcion se encarga de analizar un string recibido y determinar si se puede transformar a un numero flotante

  Parametros: Recibe un string

  Retorna: El numero si es valido, -1 en caso de contiene caracteres no numericos, -2 en caso de ser negativo, 
  y -3 en caso de que no sea ninguno de los casos anteriores
  '''
  numero_str = numero_str.strip()
  try:
    try:
      numero_float = float(numero_str)
      if (numero_float < 0):
        retorno = -2
      else:
        retorno = numero_float
    except:
      validacion = numero_str.isalnum()
      if (validacion == True):
        retorno = -1
    return retorno
  except:
      return -3  

#3.3
def sanitizar_string(valor_str:str) -> str:
  '''
  Esta funcion se encarga de analizar un string recibido y convierte todos sus caracteres a minuscula en caso que se pueda

  Parametros: Recibe un string

  Retorna: El string en minuscula en caso de ser valido, "N/A" si el string contiene numeros y 
  el valor por defecto en caso de que el string este vacio
  '''
  valor_por_defecto = "#ERROR"
  if (len(valor_str) > 0):
    valor_str = valor_str.strip()
    valor_str = valor_str.replace("/"," ")
    validacion = valor_str.replace(" ","").isalpha()
    if (validacion == True):
      valor_str = valor_str.lower()
      retorno = valor_str
    else:
      retorno = "N/A"
  else:
    retorno = valor_por_defecto
  return retorno

#3.4
def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str) -> bool:
  '''
  Esta función se encarga de sanitizar el valor del diccionario correspondiente a la clave y al tipo de dato recibido

  Parametros: Recibe un diccionario representando a un heroe, una clave representando a la key que queremos cambiar y 
  un tipo de dato que puede tomar los valores "string","entero","flotante"

  Retorna: True en caso de que se haya cambiado algun valor, False en caso contrario
  '''
  retorno = False
  if clave in heroe:
    tipo_dato = tipo_dato.lower()
    if (tipo_dato == "entero" or tipo_dato == "string" or tipo_dato == "flotante"):
      if(tipo_dato == "entero"):
        heroe[clave] = sanitizar_entero(heroe[clave])
        retorno = True
      elif(tipo_dato == "string"):
        heroe[clave] = sanitizar_string(heroe[clave])
        retorno = True
      elif(tipo_dato == "flotante"):
        heroe[clave] = sanitizar_flotante(heroe[clave])
        retorno = True
    else:
      print("Tipo de dato no reconocido")
  else:
    print("La clave especificada no existe en el héroe")
       
  return retorno

#3.5
def stark_normalizar_datos(lista_heroes:list):
  '''
  Esta función se encarga de recorrer la lista de héroes y sanitizar los valores solo de las siguientes claves: 
  ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’ e ‘inteligencia’

  Parametros: Recibe una lista de heroes

  Retorna: Imprime en pantalla "Datos normalizados" si todo sale bien, "Error" en caso contrario
  '''
  if (len(lista_heroes) > 0):
    claves_heroes = {"altura","peso","color_ojos","color_pelo","fuerza","inteligencia"}
    for heroe in lista_heroes:
      for clave in claves_heroes:
        if (clave == "fuerza"):
          sanitizar_dato(heroe,clave,"entero")
        elif (clave == "altura" or clave == "peso"):
          sanitizar_dato(heroe,clave,"flotante")
        else:
          sanitizar_dato(heroe,clave,"string")
    print("Datos normalizados")  
  else:
    print("Error: Lista de héroes vacía") 

#---------------------PUNTO 4----------------

#4.1
def generar_indice_nombres(lista_heroes:list) -> list:
  '''
  Esta función se encarga de iterar la lista de personajes y 
  generar una lista donde cada elemento es cada palabra que componen el nombre de los personajes.

  Parametros: Recibe una lista de heroes

  Retorna: Una lista con todos los nombres agrupados
  '''
  lista_valores_separados = []
  for heroe in lista_heroes:
    for clave in heroe:
      if (clave == "nombre"):
        heroe[clave] = heroe[clave].replace("-"," ")
        heroe[clave] = heroe[clave].split(" ")
        lista_valores_separados += heroe[clave]
  return lista_valores_separados         

#4.2
def stark_imprimir_indice_nombre(lista_heroes:list):
  '''
  Esta función se encarga de mostrar por pantalla el índice generado por la función generar_indice_nombres 
  con todos los nombres separados con un guión.

  Parametros: Recibe una lista de heroes
  '''
  for heroe in lista_heroes:
    if (len(lista_heroes) > 0 and type(heroe) == type({}) and "nombre" in heroe):
      validacion = True
    else:
      validacion = False
      break
  if (validacion == True):
    lista_nombre = generar_indice_nombres(lista_heroes)
    separador = "-"
    separador = separador.join(lista_nombre)
    print(separador)

#---------------------PUNTO 5----------------

#5.1
def convertir_cm_a_mtrs(valor_cm:float) -> float:
  '''
  Esta función se encarga de convertir una numero flotante a su unidad en metros

  Parametros: Recibe un valor en cm del tipo float

  Retorna: El valor pasado a metros si es un flotante positivo, -1 en caso contrario
  '''
  if (type(valor_cm) == type(float()) and valor_cm > 0):
    valor_cm = valor_cm // 100
    retorno = f"{valor_cm}m"
  else:
    retorno = -1
  return retorno

#5.2
def generar_separador(patron:str,largo:int,imprimir:bool) -> str:
  '''
  Esta función se encarga de generar un string que contenga el patrón especificado repitiendo tantas veces como la cantidad recibida como parámetro

  Parametros: Recibe un patron del tipo string, un largo del tipo entero y un bool

  Retorna: Retorna el patron que le indicamosen caso de estar todo bien, "N/A" caso contrario 
  y solo el patron en caso del que bool sea False.
  '''
  if (imprimir == True):
    if(len(patron) > 0 and len(patron) < 3 and int(largo) > 0 and int(largo) <= 235):
      patron_completo = ""
      for indice in range(largo):
        patron_completo += patron
      retorno = patron_completo
    else:
      retorno = "N/A"
  else:
    retorno = patron
  return retorno

#5.3
def generar_encabezado(titulo:str) -> str:
  '''
  Esta función se encarga de generar un string que contenga el título envuelto entre dos separadores. 

  Parametros: Recibe el un dato string que representa el titulo a generar

  Retorna: Un string con el titulo generado
  '''
  titulo = titulo.upper()
  separador = generar_separador("*",150,True)
  separador2 = generar_separador(" ",30,True)
  
  titulo_generado = ("\n{0}\n{2}{1}\n{3}".format(separador,titulo,separador2,separador))
  return titulo_generado

#5.4
def imprimir_ficha_heroe(heroe:dict):
  '''
  Esta función se encarga de imprimir la ficha de heroe. 

  Parametros: Recibe un diccionario que representa los datos del heroe
  '''
  separador = generar_separador(" ",30,True)
  nombre = heroe["nombre"]
  identidad = heroe["identidad"]
  consultora = heroe["empresa"]
  codigo = heroe["codigo"]
  altura = heroe["altura"]
  peso = heroe["peso"]
  fuerza = heroe["fuerza"]
  color_ojos = heroe["color_ojos"]
  color_pelo = heroe["color_pelo"]

  print(generar_encabezado("Principal"))
  print(f"\n{separador}NOMBRE DEL HÉROE:                                                 {nombre}\n",
        f"\n{separador}IDENTIDAD SECRETA:                                                {identidad}\n",
        f"\n{separador}CONSULTORA:                                                       {consultora}\n",
        f"\n{separador}CODIGO DE HÉROE:                                                  {codigo}\n",)
  print(generar_encabezado("Fisico"))
  print(f"\n{separador}ALTURA:                                                           {altura}\n",
        f"\n{separador}PESO:                                                             {peso}\n",
        f"\n{separador}FUERZA:                                                           {fuerza}\n")
  print(generar_encabezado("Señas particulares"))
  print(f"\n{separador}COLOR DE OJOS:                                                    {color_ojos}\n",
        f"\n{separador}COLOR DE PELO:                                                    {color_pelo}\n")

#5.3
def stark_navegar_fichas(lista_heroes:list):
  '''
  Esta función se encarga de imprimir la primer ficha de heroe en pantalla 
  y luego pedirle al usuario que ingrese una opcion para seguir navegando entre fichas

  Parametros: Recibe un diccionario que representa los datos del heroe
  '''
  posicion = 0
  while (True):
    imprimir_ficha_heroe(lista_heroes[posicion])
    print(generar_encabezado("Seguir navegando"))
    print("[ 1 ] Ir a la izquierda   [ 2 ] Ir a la derecha   [ S ] Salir\n")
    opcion = input("Ingrese una de estas opciones: ")
    if (int(opcion) == 1):
      posicion -= 1
    elif (int(opcion) == 2):
      posicion += 1
    elif (opcion == "S"):
      break              

#---------------------PUNTO 6----------------

#6.1
def imprimir_menu():
  '''
  Esta función se encarga de imprimir el menu
  '''
  separador = generar_separador("'",57,True)
  print(f"\n{separador}"
        "\n1 - Imprimir la lista de nombres junto con sus iniciales"
        "\n2 - Generar códigos de héroes"
        "\n3 - Normalizar datos"
        "\n4 - Imprimir índice de nombres"
        "\n5 - Navegar fichas"
        "\nS - Salir" 
        f"\n{separador}")

#6.2
def stark_menu_principal() -> str:
  '''
  Esta función se encarga de tomar la opcion elegida por el usuario

  Retorna: Un string que representa la opcion del usuario
  '''
  imprimir_menu()
  opcion = input("Ingrese una opcion: ")
  return opcion
