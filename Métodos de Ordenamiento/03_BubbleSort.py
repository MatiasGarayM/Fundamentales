def bubble_sort(arr):
    n = len(arr)  # Longitud de la lista
    
    # Iterar sobre cada elemento de la lista
    for i in range(n):
        # La bandera 'swapped' se usa para optimización, para terminar el algoritmo si la lista ya está ordenada
        swapped = False
        
        # Iterar sobre la lista desde el primer elemento hasta el último elemento no ordenado
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento actual es mayor que el siguiente
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Si no se realizó ningún intercambio, la lista ya está ordenada
        if not swapped:
            break
    
    return arr


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [64, 34, 25, 12, 22, 11, 90]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = bubble_sort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)