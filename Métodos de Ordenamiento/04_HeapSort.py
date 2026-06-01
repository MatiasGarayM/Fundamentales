def heapify(arr, n, i):

    largest = i      # Inicializar el más grande como la raíz
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2  # Hijo derecho

    # Si el hijo izquierdo es mayor que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Si el hijo derecho es mayor que el más grande hasta ahora
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el más grande no es la raíz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambiar
        # Recursivamente convertir el subárbol afectado en un heap
        heapify(arr, n, largest)

def heap_sort(arr):

    n = len(arr)

    # Construir un max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Mover la raíz actual al final
        heapify(arr, i, 0)  # Llamar a heapify en el heap reducido

    return arr


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [12, 11, 13, 5, 6, 7]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = heap_sort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)