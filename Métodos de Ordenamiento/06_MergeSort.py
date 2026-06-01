def merge_sort(arr):

    if len(arr) > 1:
        # Encontrar el punto medio de la lista
        mid = len(arr) // 2
        
        # Dividir la lista en dos mitades
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Llamar recursivamente a merge_sort en cada mitad
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Inicializar los índices para la sublista izquierda, derecha y lista principal
        i = j = k = 0
        
        # Copiar los datos a las listas temporales left_half y right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Verificar si quedan elementos en la lista izquierda
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Verificar si quedan elementos en la lista derecha
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    
    return arr


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [38, 27, 43, 3, 9, 82, 10]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = merge_sort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)