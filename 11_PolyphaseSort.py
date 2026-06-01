import heapq

def polyphase_sort(blocks):

    # Inicializar el heap min para manejar la fusión de los bloques
    min_heap = []
    
    # Inicializar el heap min con el primer elemento de cada bloque junto con el índice del bloque
    for i, block in enumerate(blocks):
        if block:  # Asegurarse de que el bloque no esté vacío
            heapq.heappush(min_heap, (block[0], i, 0))  # (valor, índice de bloque, índice de elemento)
    
    merged_list = []
    
    while min_heap:
        # Obtener el elemento más pequeño del heap min
        val, block_idx, element_idx = heapq.heappop(min_heap)
        
        # Agregar el elemento a la lista fusionada
        merged_list.append(val)
        
        # Mover al siguiente elemento en el bloque correspondiente
        if element_idx + 1 < len(blocks[block_idx]):
            next_tuple = (blocks[block_idx][element_idx + 1], block_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list


if __name__ == "__main__":
    # Definimos varios bloques de elementos desordenados
    bloque1 = [1, 5, 8, 10]
    bloque2 = [2, 4, 6, 7]
    bloque3 = [3, 9, 11]
    
    # Mostramos los bloques antes de la ordenación
    print("Bloque 1:", bloque1)
    print("Bloque 2:", bloque2)
    print("Bloque 3:", bloque3)
    
    # Llamamos a la función de ordenamiento
    bloques_ordenados = polyphase_sort([bloque1, bloque2, bloque3])
    
    # Mostramos los bloques ordenados después del proceso
    print("Bloques ordenados:", bloques_ordenados)