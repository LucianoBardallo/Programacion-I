import copy
import time
lista = [1,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,71,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4,2,5,0,3,7,9,4]

def buscar_minimo(lista_a_buscar:list)->int:
    minimo = 0
    for i in range(len(lista_a_buscar)):
        if(lista_a_buscar[i] < lista_a_buscar[minimo]):
            minimo = i
    return minimo


def nahuel_sort(lista_a_ordenar:list)->list:
    lista_recibida = lista_a_ordenar[:] #Shallow copy **
    lista_ordenada = []
    while(len(lista_recibida) > 0):
        minimo = buscar_minimo(lista_recibida)
        elemento_minimo = lista_recibida.pop(minimo)
        lista_ordenada.append(elemento_minimo)
    
    return lista_ordenada

def ivan_sort(lista_a_ordenar:list)->list:
    lista_recibida = lista_a_ordenar[:] #Shallow copy **
    flag_swap = True
    limite = 1
    while(flag_swap == True):
        flag_swap = False
        for i in range(len(lista_recibida) - limite):
            if(lista_recibida[i] > lista_recibida[i+1]):
                lista_recibida[i],lista_recibida[i+1] = lista_recibida[i+1],lista_recibida[i]
                flag_swap = True
        limite += 1
    return lista_recibida

def qsort(lista_a_ordenar:list)->list:
    lista_recibida = lista_a_ordenar[:] #Shallow copy **
    lista_de = []
    lista_iz = []
    if(len(lista_a_ordenar) <= 1):
        return lista_a_ordenar
    else:
        pivot = lista_a_ordenar[0]
        for elemento in lista_recibida[1:]:
            if(elemento > pivot):
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)    

    lista_iz = qsort(lista_iz)
    lista_iz.append(pivot)
    lista_de = qsort(lista_de)
    return lista_iz + lista_de


inicio = time.time()
lista_resultado = nahuel_sort(lista)
fin = time.time()
print("Nahuel",(fin - inicio)*1000)


inicio = time.time()
lista_resultado = ivan_sort(lista)
fin = time.time()
print("Ivan",(fin - inicio)*1000)

inicio = time.time()
lista_resultado = qsort(lista)
fin = time.time()
print("Qsort",(fin - inicio)*1000)
print(lista_resultado[:50])