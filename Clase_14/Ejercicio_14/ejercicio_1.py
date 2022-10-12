lista_precios = {
    
    "banana" : {
        "precio" : 120.10,
        "unidad_medida": "kg",
        "stock": 50
    },
    
    "pera": {
        "precio": 240.50,
        "unidad_medida": "kg",
        "stock": 40        
    },
    
    "frutilla": {
        "precio": 300,
        "unidad_medida": "kg",
        "stock": 100        
    }, 
    
    "mango" : {
        "precio": 300,
        "unidad_medida": "unidad",
        "stock": 100  
    }

}

# Punto 1: solicitar al usuario un producto y verificiar si existe en 'lista_precios' en caso de existir mostrar precio y el stock. En caso de no existir el 
# producto mostrar el mensaje 'el articulo no se encuentra en la lista'

# Punto 2: agregar al punto anterior que el usuario ingrese la cantidad y retornar el precio total (precio * cantidad)

# Punto 3: solicitar al usuario que ingrese una nueva fruta junto con su precio, unidad de medida y stock. Agregar la nueva fruta a la lista de precios

# Punto 4: imprimir el listado de frutas (solo su nombre)

# Punto 5: solicitarle al usuario el nombre de fruta y en caso de exisitir eliminarla. En caso de que el producto no exista mostrar 
# el mensaje 'el articulo no se encuentra en la lista'


producto_buscado = input("Ingrese el producto a buscar: ")
cantidad = input("Ingrese la cantidad: ")
if producto_buscado in lista_precios:
    precio = lista_precios[producto_buscado]["precio"]
    cantidad_total = int(cantidad) * precio
    print("Precio: {0} c/u\nStock: {1}\nPrecio Total: {2}".format(lista_precios[producto_buscado]["precio"],lista_precios[producto_buscado]["stock"],cantidad_total))
else:
    print("El articulo no se encuentra en la lista")

nombre_fruta = input("Ingrese una nueva fruta: ")
precio_fruta = input("Ingrese el precio de la fruta: ")
unidad_de_medida = input("Ingrese la unidad de medida: ")
stock = input("Ingrese el stock disponible: ") 
dic_fruta = {nombre_fruta: {"precio":precio_fruta,"unidad de medida":unidad_de_medida,"stock":stock}}

lista_precios.update(dic_fruta)
print(lista_precios)

print(list(lista_precios.keys()))

nombre_fruta = input("Ingrese el nombre de la fruta: ")
if nombre_fruta in lista_precios:
    lista_precios.pop(nombre_fruta)
    print(f"Se ha eliminado {nombre_fruta} de la lista")
else:
    print("El articulo no se encuentra en la lista")
print(lista_precios)