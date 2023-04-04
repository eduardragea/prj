import random
import time
import struct
 
length = 1
max_length = 300000
 
def read():
    global length
    with open("random.dat", "rb") as fin:
        data = fin.read()
        int_list = []
        for i in range(0, len(data), 4):
            int_value = struct.unpack('<i', data[i:i+4])[0]
            int_list.append(int_value)
        return int_list

 
def bubbleSort():
    global length, list
    for i in range(length):
        for j in range(length-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(list, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(list, l, m)
        mergeSort(list, m+1, r)
        merge(list, l, m, r)
 
def insertionSort():
    global length, list
    for i in range(1, length):
        temp = list[i]
        j = i-1
        while j >= 0 and list[j] > temp:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = temp
 
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
 
while length <= max_length:
    print(f"\nLength\t: {length}")
    list = read()
    t1 = time.perf_counter()
    mergeSort(list, 0, length - 1)
    t2 = time.perf_counter()
    print(f"Merge Sort\t: {t2-t1:.6f} sec")
    list = read()
    t1 = time.perf_counter()
    insertionSort()
    t2 = time.perf_counter()
    print(f"Insertion Sort\t: {t2-t1:.6f} sec")
    list = read()
    t1 = time.perf_counter()
    quickSort(0, length-1)
    t2 = time.perf_counter()
    print(f"Quick Sort\t: {t2-t1:.6f} sec")
    if(length<10):
        length = length + 1
    else:
        length = length * 10
