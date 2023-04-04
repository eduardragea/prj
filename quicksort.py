from generate import read
import time
import random

# def partition(array, low, high):
#     pivot = array[high]
#     i = low - 1
#     for j in range(low, high):
#         if array[j] <= pivot:
#             i = i + 1
#             (array[i], array[j]) = (array[j], array[i])
#     (array[i + 1], array[high]) = (array[high], array[i + 1])
#     return i + 1
 
def medianQuicksort(arr, left, right):
    if left >= right:
        return
    
    # Find the median of the first, last, and middle elements as the pivot
    mid = (left + right) // 2
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[mid] > arr[right]:
        arr[mid], arr[right] = arr[right], arr[mid]
    if arr[left] > arr[mid]:
        arr[left], arr[mid] = arr[mid], arr[left]
    pivot = arr[mid]
    
    # Partition the array
    i = left
    j = right
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    # Recursively sort the two sub-arrays
    medianQuicksort(arr, left, j)
    medianQuicksort(arr, i, right)

def iterativeQuicksort(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        pivot = random.choice(arr)
        i = start
        j = end
        
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        # Simulate recursive calls using loop
        if j - start < end - i:
            stack_top = end
            end = j
            j = stack_top
        else:
            stack_top = start
            start = i
            i = stack_top
    
    return arr

def recursiveQuicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    left = recursiveQuicksort(left)
    right = recursiveQuicksort(right)

    return left + [pivot] + right

def stackQuicksort(arr):
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

def partition(left, right):
    global list
    pivot_element = list[left]
    lb = left
    ub = right
    while left < right:
        while list[left] <= pivot_element:
            left += 1
        while list[right] > pivot_element:
            right -= 1
        if left < right:
            list[left], list[right] = list[right], list[left]
    list[lb] = list[right]
    list[right] = pivot_element
    return right
 
def quickSort(left, right):
    if left < right:
        pivot = partition(left, right)
        quickSort(left, pivot-1)
        quickSort(pivot+1, right)

for i in range(0,5):
    length = 1
    max_length = 100000
    while length <= max_length:
        print(f"\nLength\t: {length}")
        list = read()
        if i == 0:
            t1 = time.perf_counter()
            recursiveQuicksort(list)
            t2 = time.perf_counter()
            print(f"Recursive Quick Sort\t: {t2-t1:.6f} sec")
        elif i == 1:
            t1 = time.perf_counter()
            iterativeQuicksort(list)
            t2 = time.perf_counter()
            print(f"Iterative Quick Sort\t: {t2-t1:.6f} sec")
        elif i == 2:
            t1 = time.perf_counter()
            stackQuicksort(list)
            t2 = time.perf_counter()
            print(f"Stack Quick Sort\t: {t2-t1:.6f} sec")
        elif i == 3:
            t1 = time.perf_counter()
            medianQuicksort(list, 0, length - 1)
            t2 = time.perf_counter()
            print(f"Median Quick Sort\t: {t2-t1:.6f} sec")
        else:
            t1 = time.perf_counter()
            quickSort(0, length - 1)
            t2 = time.perf_counter()
            print(f"Partition Quick Sort\t: {t2-t1:.6f} sec")
        if(length<10):
            length = length + 1
        else:
            length = length * 10

