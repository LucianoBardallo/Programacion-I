'''
La división de alimentos de industrias Wayne está trabajando en un pequeño software para cargar datos de heroínas y héroes, 
para tener un control de las condiciones de heroes existentes, nos solicitan:
Nombre de Heroína/Héroe
EDAD (mayores a 18 años)
Sexo ("m", "f" o "nb")
Habilidad ("fuerza", "magia", "inteligencia").
A su vez, el programa deberá mostrar por consola lo siguiente:
Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
El sexo y nombre de Heroe | Heroína de mayor edad.
La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
El promedio de edad entre Heroinas.
El promedio de edad entre Heroes de fuerza.
'''
respuesta = "s"
flag = 0
flag2 = 0
contador_femenino_habilidad = 0
contador_masculino = 0
contador_femenino = 0
acumulador_edad_masculino_fuerza = 0
acumulador_edad_femenino = 0

while (respuesta == "s"):
    nombre = input("Nombre de Heroína/Héroe: \n")

    edad = input("Edad de Heroína/Heroe: \n")
    edad = int(edad)
    while (edad < 18):
        edad = input("Edad de Heroína/Heroe: \n")
        edad = int(edad)

    sexo = input("Sexo de Heroína/Heroe (Masculino / Femenino / No binario): \n")
    while (sexo != "Masculino" and sexo != "Femenino" and sexo != "No binario"):
        sexo = input("Sexo de Heroína/Heroe (Masculino / Femenino / No binario): \n")

    habilidad = input("Habilidad de Heroína/Heroe (Fuerza / Magia / Inteligencia): \n")
    while (habilidad != "Fuerza" and habilidad != "Magia" and habilidad != "Inteligencia"):
        habilidad = input("Habilidad de Heroína/Heroe (Fuerza / Magia / Inteligencia): \n")


    if (habilidad == "Fuerza"):
        if (flag == 0 or fuerza_mas_joven > edad):
            fuerza_mas_joven = edad
            nombre_mas_joven = nombre
            flag = 1
        if (sexo == "Masculino"):
            contador_masculino += 1
            acumulador_edad_masculino_fuerza += edad

    if (flag2 == 0 or mayor_edad < edad):
        mayor_edad = edad
        nombre_mayor_edad = nombre
        sexo_mayor_edad = sexo
        flag2 = 1

    if (sexo == "Femenino"):
        contador_femenino += 1
        acumulador_edad_femenino += edad
        if (habilidad == "Fuerza" or habilidad == "Magia"):
            contador_femenino_habilidad += 1

    respuesta = input("Quiere continuar? (s): ")        

promedio_edad_femenino = acumulador_edad_femenino / contador_femenino
promedio_edad_masculino_fuerza = acumulador_edad_masculino_fuerza / contador_masculino

print(f"El nombre de Héroe / Heroína de fuerza mas joven es: {nombre_mas_joven} con {fuerza_mas_joven} años")
print(f"El sexo y nombre de Héroe / Heroína de mayor edad es: {nombre_mayor_edad} con {mayor_edad} años ({sexo_mayor_edad})")
print(f"La cantidad de Heroinas que tienen habilidades de Fuerza o Magia es: {contador_femenino_habilidad}")
print(f"El promedio de edad entre Heroinas es: {promedio_edad_femenino}")
print(f"El promedio de edad entre Heroes de Fuerza es: {promedio_edad_masculino_fuerza}")
