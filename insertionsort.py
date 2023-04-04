from generate import read
import time

def insertionSort(arr):
    global length, list
    for i in range(1, length):
        temp = list[i]
        j = i-1
        while j >= 0 and list[j] > temp:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = temp

length = 1
max_length = 100000
while length <= max_length:
    print(f"\nLength\t: {length}")
    list = read()
    t1 = time.perf_counter()
    insertionSort(list)
    t2 = time.perf_counter()
    print(f"Insertion Sort\t: {t2-t1:.6f} sec")
    if(length<10):
        length = length + 1
    else:
        length = length * 10