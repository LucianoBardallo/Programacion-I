'''
La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para la cocina de Industrias Wayne. 
Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
PESO: (entre 10 y 100 kilos)
PRECIO POR KILO: (mayor a 0 [cero]).
TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto. 
o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.
El importe total a pagar, BRUTO sin descuento.
El importe total a pagar con descuento (Solo si corresponde).
Informar el tipo de alimento más caro.
El promedio de precio por kilo en total.
'''
respuesta = "s"
acumulador_a_pagar = 0
flag = 0
contador_precio_kilo = 0
acumulador_precio_kilo = 0
acumulador_peso = 0

while(respuesta == "s"):
    peso = input("Ingrese el peso: \n")
    peso = float(peso)
    while(peso < 10 and peso > 100):
        peso = input("Ingrese el peso: \n")
        peso = float(peso)

    precio_kilo = input("Ingrese el precio por kilo: \n")
    precio_kilo = float(precio_kilo)
    while(precio_kilo <= 0):
        precio_kilo = input("Ingrese el precio por kilo: \n")
        precio_kilo = float(precio_kilo)

    tipo = input("Ingrese el tipo (vegetal /animal /mezcla): \n")
    while(tipo != "vegetal" and tipo != "animal" and tipo != "mezcla"):
        tipo = input("Ingrese el tipo (vegetal /animal /mezcla): \n")

    total_a_pagar = peso * precio_kilo
    acumulador_a_pagar += total_a_pagar
    acumulador_precio_kilo += precio_kilo
    acumulador_peso += peso
    contador_precio_kilo += 1

    if (flag == 0 or alimento_mas_caro < precio_kilo):
        alimento_mas_caro = precio_kilo
        tipo_mas_caro = tipo
        flag = 1
        
    respuesta = input("¿Quiere continuar? (s/n) ")

if (acumulador_peso > 100):
    descuento_escrito = "15%"
    descuento_obtenido = 0.15
elif (acumulador_peso > 300):
    descuento_escrito = "25%"
    descuento_obtenido = 0.25

descuento = acumulador_a_pagar * descuento_obtenido
importe_con_descuento = acumulador_a_pagar - descuento  
promedio = acumulador_precio_kilo / contador_precio_kilo

print(f"El importe bruto es: ${acumulador_a_pagar}")
print(f"El descuento es del: {descuento_escrito}")
print(f"El importe con descuento es: {importe_con_descuento}")
print(f"El tipo de alimento mas caro es: {tipo_mas_caro}")
print(f"El promedio de precio por kilo es: {promedio}")
