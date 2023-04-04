from generate import read
import time

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

def insertionSort(arr):
    global length, list
    for i in range(1, length):
        temp = list[i]
        j = i-1
        while j >= 0 and list[j] > temp:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = temp

def hybridSort(left, right, threshold=10):
    global length, list
    if len(list) <= threshold:
        return insertionSort(list)
    if left < right:
        pivot = partition(left, right)
        hybridSort(left, pivot-1)
        hybridSort(pivot+1, right)

length = 1
max_length = 100000
while length <= max_length:
    print(f"\nLength\t: {length}")
    list = read()
    t1 = time.perf_counter()
    hybridSort(0, length-1)
    t2 = time.perf_counter()
    print(f"Quick Sort\t: {t2-t1:.6f} sec")
    if(length<10):
        length = length + 1
    else:
        length = length * 10
