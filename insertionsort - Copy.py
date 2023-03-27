def insertionSort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i-1
        while j >= 0 and arr[j] > curr:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = curr
    return arr