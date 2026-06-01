def quicksort(arr):

    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(arr) <= 1:
        return arr
    else:
        # Elegir un pivote (aquí elegimos el pivote como el primer elemento)
        pivot = arr[0]
        
        # Dividir la lista en sublistas: menores, iguales y mayores al pivote
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        
        # Ordenar recursivamente las sublistas y combinarlas con el pivote
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [10, 7, 8, 9, 1, 5]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = quicksort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)