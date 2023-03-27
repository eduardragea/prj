def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
 
def quickSort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quickSort(array, low, pivot - 1)
        quickSort(array, pivot + 1, high)

def iterativeQuicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    left = quicksort(left)
    right = quicksort(right)

    return left + [pivot] + right

def stacQuicksort(arr):
    stack = [(0, len(arr)-1)]
    while stack:
        start, end = stack.pop()
        if end - start < 1:
            continue

        pivot = arr[start]
        i = start + 1
        j = end

        while i <= j:
            while i <= j and arr[i] < pivot:
                i += 1
            while i <= j and arr[j] >= pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        arr[start], arr[j] = arr[j], arr[start]
        stack.append((start, j - 1))
        stack.append((j + 1, end))

    return arr

def hybrid_sort(arr, threshold=10):
    if len(arr) <= threshold:
        return insertion_sort(arr)
    
    pivot = arr[0]
    left = []
    right = []
    
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    left = hybrid_sort(left, threshold)
    right = hybrid_sort(right, threshold)
    
    return left + [pivot] + right

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

