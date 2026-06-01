import heapq

def initial_runs_sort(data, block_size):

    n = len(data)
    runs = []
    
    # Generar ejecuciones iniciales
    for i in range(0, n, block_size):
        run = data[i:i + block_size]
        run.sort()
        runs.append(run)
    
    # Fusionar ejecuciones iniciales
    sorted_data = merge_runs(runs)
    
    return sorted_data

def merge_runs(runs):

    min_heap = []
    
    # Inicializar el heap min con el primer elemento de cada ejecución
    for i, run in enumerate(runs):
        if run:  # Asegurarse de que la ejecución no esté vacía
            heapq.heappush(min_heap, (run[0], i, 0))  # (valor, índice de ejecución, índice de elemento)
    
    merged_list = []
    
    while min_heap:
        # Obtener el elemento más pequeño del heap min
        val, run_idx, element_idx = heapq.heappop(min_heap)
        
        # Agregar el elemento a la lista fusionada
        merged_list.append(val)
        
        # Mover al siguiente elemento en la ejecución correspondiente
        if element_idx + 1 < len(runs[run_idx]):
            next_tuple = (runs[run_idx][element_idx + 1], run_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [12, 11, 13, 5, 6, 7, 19, 4, 2, 10, 3, 14]
    block_size = 4  # Tamaño del bloque para las ejecuciones iniciales
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = initial_runs_sort(ejemplo_lista, block_size)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)