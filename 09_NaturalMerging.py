def merge(arr, left, mid, right):

    # Crear arrays temporales para los subarrays
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    # Inicializar índices para fusionar los subarrays
    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar los elementos restantes de L[], si hay alguno
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar los elementos restantes de R[], si hay alguno
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def natural_merge_sort(arr):

    # Función para encontrar sublistas ordenadas
    def find_runs(arr):
        runs = []
        n = len(arr)
        new_run = [0]
        
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                runs.append((new_run[0], i - 1))
                new_run = [i]
        
        runs.append((new_run[0], n - 1))
        return runs
    
    # Ejecutar el algoritmo de ordenamiento
    if len(arr) <= 1:
        return arr
    
    runs = find_runs(arr)
    
    while len(runs) > 1:
        new_runs = []
        
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                left, mid = runs[i]
                _, right = runs[i + 1]
                merge(arr, left, mid, right)
                new_runs.append((left, right))
            else:
                new_runs.append(runs[i])
        
        runs = new_runs
    
    return arr


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [12, 11, 13, 5, 6, 7, 19, 4, 2, 10, 3, 14]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = natural_merge_sort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)