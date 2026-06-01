import heapq

def balanced_multiway_merge(lists):

    # Usamos un heap min para mantener el orden en el que vamos a fusionar los elementos
    min_heap = []
    
    # Inicializamos el heap min con el primer elemento de cada lista junto con el índice de la lista
    for i, lst in enumerate(lists):
        if lst:  # Aseguramos que la lista no esté vacía
            heapq.heappush(min_heap, (lst[0], i, 0))  # (valor, índice de lista, índice de elemento)
    
    merged_list = []
    
    while min_heap:
        # Obtenemos el menor elemento del heap min
        val, list_idx, element_idx = heapq.heappop(min_heap)
        
        # Agregamos el elemento a la lista fusionada
        merged_list.append(val)
        
        # Movemos al siguiente elemento en la lista correspondiente
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list


if __name__ == "__main__":
    # Definimos varias listas ordenadas de ejemplo
    lista1 = [1, 3, 5, 7]
    lista2 = [2, 4, 6, 8, 10]
    lista3 = [0, 9, 11]
    
    # Mostramos las listas antes de la fusión
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Lista 3:", lista3)
    
    # Llamamos a la función de fusión
    listas_fusionadas = balanced_multiway_merge([lista1, lista2, lista3])
    
    # Mostramos la lista fusionada después del proceso
    print("Listas fusionadas:", listas_fusionadas)