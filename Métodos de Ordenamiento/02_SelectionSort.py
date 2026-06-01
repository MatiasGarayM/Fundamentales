def selection_sort(arr):

    n = len(arr)  # Longitud de la lista
    
    # Iterar sobre cada elemento de la lista
    for i in range(n):
        # Suponer que el primer elemento no ordenado es el menor
        min_idx = i
        
        # Encontrar el menor elemento en la sublista no ordenada
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Intercambiar el menor elemento encontrado con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [64, 25, 12, 22, 11]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = selection_sort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)