#----------------ORDENAMIENTO----------------

lista = [14,5,20,10,23,15,7,16,29,21,-102,99,0]

def buscar_minimo(lista:list):
    minimo = 0
    for i in range(len(lista)):
        if (lista[minimo] > lista[i]):
            minimo = i
    return minimo        

def ordenar_dato(lista:list):
    lista_recibida = lista[:]
    lista_ordenada = []
    while(len(lista_recibida) > 0):
        minimo = buscar_minimo(lista_recibida)
        lista_ordenada.append(lista_recibida.pop(minimo))
    return lista_ordenada   

print(f'''\nLista Original: {lista}
          \nLista Ordenada: {ordenar_dato(lista)}''')

'''
--- Pasos a seguir ---
1- Primero recibo la lista
2- Hago una copia de la lista original
3- Creo una lista nueva
4- Busco la posicion del elemento minimo de la lista recibida
5- Retorno la posicion del elemento minimo
6- Cuando lo encuentro lo agrego a una lista nueva 
y lo saco de la otra lista
7- Repito lo mismo hasta que la primer listas quede vacia
'''