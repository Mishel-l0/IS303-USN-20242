import random
import time

# Funciones de ordenamiento
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Generar una lista aleatoria
n = 10000  # Cambia a 100000 para más datos
random_list = [random.randint(1, 10000) for _ in range(n)]

# Medir el tiempo de cada método
results = {}

# Bubble Sort
start_time = time.time()
bubble_sort(random_list.copy())
results['Bubble Sort'] = time.time() - start_time

# Selection Sort
start_time = time.time()
selection_sort(random_list.copy())
results['Selection Sort'] = time.time() - start_time

# Insertion Sort
start_time = time.time()
insertion_sort(random_list.copy())
results['Insertion Sort'] = time.time() - start_time

# Merge Sort
start_time = time.time()
merge_sort(random_list.copy())
results['Merge Sort'] = time.time() - start_time

# Imprimir los resultados
for name, duration in results.items():
    print(f"{name}: {duration:.2f} segundos")
