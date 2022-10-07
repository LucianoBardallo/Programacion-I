# MIT License
#
# Copyright (c) 2022 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

lista_palabras = [
    "goKU", "vEgETa", "FrIEzA", "CELl", "BeERuS", 'kriLLin'
]

# Refactorizar a la version clasica de la funcion
superficie_circulo = lambda x: pow(x, 2) * 3.1415

def calcular_superficie(x:int,y:int) -> float:
    superficie = pow(x,y) * 3.1415
    return superficie
print(f'Superficie de circulo: {round(calcular_superficie(15,2))}')

# Refactorizar a la version clasica
minisculizar = lambda x: str(x).lower()
def minisculizar(lista:list) -> list:
    lista_copia = lista[:]
    for i in range(len(lista_copia)):
        lista_copia[i] = lista_copia[i].lower()
    return lista_copia
print(f'Lista Minuscula: {minisculizar(lista_palabras)}')

# Refactorizar a la version clasica
capitalizar = lambda x: str(x).capitalize()
lista_mapeada = list(map(capitalizar, lista_palabras))
def capitalizar_lista(lista:list) -> list:
    lista_capitalizada = lista[:]
    for i in range(len(lista_capitalizada)):
        lista_capitalizada[i] = lista_capitalizada[i].capitalize()
    return lista_capitalizada
print(f'Lista Capitalizada: {capitalizar_lista(lista_palabras)}')

heroes = [
    "goKU", "vEgETa", 'kriLLin'
]

villanos = [
    "FrIEzA", "CELl", "Majin Buu"
]

ataques = [
    "Kame hame ha", "Final flash", "Kienzan"
]

#for heroe, ataque, villano in zip(heroes, ataques, villanos):
#    print(f'{heroe.capitalize()} Lanza un {ataque.capitalize()} a {villano.capitalize()}')

def mostrar_secuencia_ataque(list1:list,list2:list,list3:list):
    for z in range(len(list1)):
        for x in range(z, len(list2)):
            for c in range(x, len(list3)):
                mensaje = "{0} Lanza un {1} a {2}".format(list1[z].capitalize(),list2[x].capitalize(),list3[c].capitalize())
                print(mensaje)
                break
            break

mostrar_secuencia_ataque(heroes,ataques,villanos)