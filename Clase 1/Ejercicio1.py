#La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
#El tipo (validar "barbijo", "jabón" o "alcohol")
#El precio: (validar entre 100 y 300)
#La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
#La marca y el Fabricante.

# Se debe informar lo siguiente:
#Del más caro de los barbijos, la cantidad de unidades y el fabricante.
#Del ítem con más unidades, el fabricante.
#Cuántas unidades de jabones hay en total.

flag = 0
flag2 = 0
acumulador_jabon = 0

for i in range(5):
    tipo = input("Ingrese el tipo de producto 'barbijo', 'jabon', 'alcohol':  \n ")
    while (tipo != "jabon" and tipo != "barbijo" and tipo != "alcohol"):
        tipo = input("Ingrese el tipo de producto 'barbijo', 'jabon', 'alcohol':  \n ")

    precio = input("Ingrese el precio entre 100 y 300: \n")
    precio = float(precio)
    while (precio < 100 or precio > 300):
        precio = input("Ingrese el precio entre 100 y 300: \n")
        precio = float(precio)

    cantidad_unidades = input("Ingrese la cantidad de unidades: \n")
    cantidad_unidades = int(cantidad_unidades)
    while (cantidad_unidades <= 0 or cantidad_unidades > 1000):
        cantidad_unidades = input("Ingrese la cantidad de unidades: \n")
        cantidad_unidades = int(cantidad_unidades)

    marca = input("Ingrese la marca: \n")
    fabricante = input("Ingrese el fabricante: \n")

    if (flag == 0 or barbijo_mas_caro < precio):
        barbijo_mas_caro = precio
        fabricante_barbijo = fabricante
        cantidad_barbijo = cantidad_unidades
        flag = 1

    if (flag2 == 0 or item_mas_unidades < cantidad_unidades):
        item_mas_unidades = cantidad_unidades
        fabricante_mas_unidades = fabricante
        flag2 = 1

    if (tipo == "jabon"):
        acumulador_jabon += cantidad_unidades

print(f"El mas caro de los barbijos tiene una cantidad de:  {cantidad_barbijo}  y es fabricado por {fabricante_barbijo} ")
print(f"El item con mas unidades es de fabricante:  {fabricante_mas_unidades} y tiene {item_mas_unidades}  unidades")
print(f"La cantidad de jabones es: ({acumulador_jabon}")
print(f"Gracias por usar el programa")