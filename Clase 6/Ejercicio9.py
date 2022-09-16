from calendar import c
from csv import list_dialects
from data_stark import lista_personajes

'''
lista_heroes =
[
 {
   "nombre": "Howard the Duck",
   "identidad": "Howard (Last name unrevealed)",
   "empresa": "Marvel Comics",
   "altura": "79.349999999999994",
   "peso": "18.449999999999999",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Yellow",
   "fuerza": "2",
   "inteligencia": "average"
 },
 {
   "nombre": "Rocket Raccoon",
   "identidad": "Rocket Raccoon",
   "empresa": "Marvel Comics",
   "altura": "122.77",
   "peso": "25.73",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Brown",
   "fuerza": "5",
   "inteligencia": "average"
 }
]

'''
#---------------------PUNTO 1----------------

#1.1
def extraer_iniciales(nombre_heroe:str):
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

#for personaje in lista_personajes:
#  print(extraer_iniciales(personaje["nombre"]))

#1.2
def definir_iniciales_nombre(heroe:dict)->bool:
  retorno = False 
  if (type(heroe) == type(dict()) and len(heroe["nombre"]) > 0):
    iniciales = extraer_iniciales(heroe["nombre"])
    heroe["iniciales"] = iniciales
    retorno = True
  
  return retorno

#for personaje in lista_personajes:
#  print(definir_iniciales_nombre(personaje) ) 

#1.3
def agregar_iniciales_nombre(lista_heroes:list) -> bool:
  
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

#print(agregar_iniciales_nombre(lista_personajes))
#print(lista_personajes)

#1.3
def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
  if (type(lista_heroes) == type([]) and len(lista_heroes) > 0):
    agregar_iniciales_nombre(lista_heroes)
    for heroe in lista_heroes:
      agregar_iniciales_nombre(heroe)
      print("*{0} - ({1})".format(heroe["nombre"],heroe["iniciales"]))
    

#stark_imprimir_nombres_con_iniciales(lista_personajes)

#---------------------PUNTO 2----------------

#2.1
def generar_codigo_heroe(id_heroe:int,genero_heroe:str):
  if (type(id_heroe) == type(int()) and len(genero_heroe) > 0 and (genero_heroe == "F" or genero_heroe == "M" or genero_heroe == "NB")):
    id_heroe = str(id_heroe)
    if (genero_heroe == "NB"):
      id_heroe = id_heroe.zfill(7) 
    else:
      id_heroe = id_heroe.zfill(8)  
    codigo_heroe = "{0}-{1}".format(genero_heroe,id_heroe)
    return codigo_heroe

generar_codigo_heroe(15,"F")

#2.2
def agregar_codigo_heroe(heroe:dict):
  retorno = False
  if (len(heroe) > 0):
    codigo_heroe = generar_codigo_heroe(heroe["posicion"],heroe["genero"])
    if(len(codigo_heroe) == 10):
      heroe["codigo"] = codigo_heroe
      retorno = True
  return retorno

#agregar_codigo_heroe(lista_personajes[0])

#2.3
def stark_generar_codigos_heroes(lista_heroes:list):
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

stark_generar_codigos_heroes(lista_personajes)   

#---------------------PUNTO 3----------------

#3.1
def sanitizar_entero(numero_str:str):
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
  
#print(sanitizar_entero("323.2"))

#3.2
def sanitizar_flotante(numero_str:str):
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

#print(sanitizar_flotante("3.2"))

#3.3
def sanitizar_string(valor_str:str):
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

#print(sanitizar_string("SDdS/Ddsa"))

#3.4
def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str):
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


#stark_normalizar_datos(lista_personajes)

#---------------------PUNTO 4----------------

#4.1
def generar_indice_nombres(lista_heroes:list):
  lista_valores_separados = []
  for heroe in lista_heroes:
    for clave in heroe:
      if (clave == "nombre"):
        heroe[clave] = heroe[clave].replace("-"," ")
        heroe[clave] = heroe[clave].split(" ")
        lista_valores_separados += heroe[clave]
  return lista_valores_separados         

#generar_indice_nombres(lista_personajes)

#4.2
def stark_imprimir_indice_nombre(lista_heroes:list):
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
      
#stark_imprimir_indice_nombre(lista_personajes)

#---------------------PUNTO 5----------------

#5.1
def convertir_cm_a_mtrs(valor_cm:float):
  if (type(valor_cm) == type(float()) and valor_cm > 0):
    valor_cm = valor_cm // 100
    retorno = f"{valor_cm}m"
  else:
    retorno = -1
  return retorno

#print(convertir_cm_a_mtrs(1000.0))  

#5.2
def generar_separador(patron:str,largo:int,imprimir:bool):
  if (imprimir == True):
    if(len(patron) > 0 and len(patron) < 3):
      patron_completo = ""
      for indice in range(largo):
        patron_completo += patron
      retorno = patron_completo
    else:
      retorno = "N/A"
  else:
    retorno = patron
  return retorno


#print(generar_separador("#",3,True))

#5.3
def generar_encabezado(titulo:str):
  titulo = titulo.upper()
  separador = generar_separador("*",150,True)
  separador2 = generar_separador(" ",30,True)
  
  print("\n{0}\n{2}{1}\n{3}".format(separador,titulo,separador2,separador))
 
#generar_encabezado("principal")

#5.4
def imprimir_ficha_heroe(heroe:dict):
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

  generar_encabezado("Principal")
  print(f"\n{separador}NOMBRE DEL HÉROE:                                                 {nombre}\n",
        f"\n{separador}IDENTIDAD SECRETA:                                                {identidad}\n",
        f"\n{separador}CONSULTORA:                                                       {consultora}\n",
        f"\n{separador}CODIGO DE HÉROE:                                                  {codigo}\n",)
  generar_encabezado("Fisico")
  print(f"\n{separador}ALTURA:                                                           {altura}\n",
        f"\n{separador}PESO:                                                             {peso}\n",
        f"\n{separador}FUERZA:                                                           {fuerza}\n")
  generar_encabezado("Señas particulares")
  print(f"\n{separador}COLOR DE OJOS:                                                    {color_ojos}\n",
        f"\n{separador}COLOR DE PELO:                                                    {color_pelo}\n")
        

#imprimir_ficha_heroe(lista_personajes[1])

#5.3
def stark_navegar_fichas(lista_heroes:list):
  posicion = 0
  while (True):
    imprimir_ficha_heroe(lista_heroes[posicion])
    generar_encabezado("Seguir navegando")
    print("[ 1 ] Ir a la izquierda   [ 2 ] Ir a la derecha   [ S ] Salir\n")
    opcion = input("Ingrese una de estas opciones: ")
    if (int(opcion) == 1):
      posicion -= 1
    elif (int(opcion) == 2):
      posicion += 1
    elif (opcion == "S"):
      break

stark_navegar_fichas(lista_personajes)                

'''
{
   "nombre": "Howard the Duck",
   "identidad": "Howard (Last name unrevealed)",
   "empresa": "Marvel Comics",
   "altura": "79.349999999999994",
   "peso": "18.449999999999999",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Yellow",
   "fuerza": "2",
   "inteligencia": "average"
 },
'''