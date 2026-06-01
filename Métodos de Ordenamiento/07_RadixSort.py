def counting_sort_for_radix(arr, exp):

    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Contar las ocurrencias de cada dígito en exp
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Cambiar count[i] para que contenga la posición actual de este dígito en output
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Construir el array de salida
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    
    # Copiar los elementos ordenados de output a arr
    for i in range(n):
        arr[i] = output[i]
    
    return arr

def radix_sort(arr):

    # Encontrar el número máximo para conocer el número de dígitos
    max_val = max(arr)
    
    # Aplicar Counting Sort a cada dígito (exp será 1, 10, 100, ...)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    
    return arr


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [170, 45, 75, 90, 802, 24, 2, 66]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = radix_sort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)