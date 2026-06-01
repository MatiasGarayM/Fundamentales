def insertion_sort(arr):

    # Iterar sobre cada elemento de la lista comenzando desde el segundo elemento
    for i in range(1, len(arr)):
        key = arr[i] # Elemento actual a insertar en la parte ordenada
        j = i - 1 # Índice del último elemento de la parte ordenada

        # Mover elementos de la parte ordenada que son mayores que la 'key'
        # una posición hacia la derecha para hacer espacio para la 'key'
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insertar la 'key' en la posición correcta
        arr[j + 1] = key
    
    return arr

if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [12, 11, 13, 5, 6]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = insertion_sort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)