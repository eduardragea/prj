from quicksort import quickSort,iterativeQuicksort
from mergesort import mergeSort
from insertionsort import insertionSort

import random
import sys
from timeit import default_timer as timer

def randomInputGenerator(n):
    i = 0
    data = []
    while i < n:
        data.append(random.randint(-n, n))
        i += 1
    return data

def allOnesGenerator(n):
    i = 0
    data = []
    while i < n:
        data.append(1)
        i += 1
    return data

def descendingGenerator(n):
    data = []
    while n:
        data.append(n)
        n -= 1
    return data

def ascendingGenerator(n):
    i = 0
    data = []
    while i < n:
        data.append(i)
        i += 1
    return data

sys.setrecursionlimit(1000000)
# data = randomInputGenerator(100000000)
# dataCopy = data
# start = timer()
# size = len(dataCopy)

# quickSort(dataCopy, 0, size - 1)
# end = timer()
# print(end-start)

# dataCopy = data
# start = timer()
# size = len(dataCopy)
# mergeSort(dataCopy, 0, size - 1)
# end = timer()
# print(end - start)

# dataCopy = data
# start = timer()
# insertionSort(dataCopy)
# end = timer()
# print(end - start)

i = 1
while i <= 1000000000:
    print(i)
    data = randomInputGenerator(i)
    dataCopy = data
    start = timer()
    size = len(dataCopy)

    quickSort(dataCopy, 0, size - 1)
    end = timer()
    print((end-start)*1000)

    dataCopy = data
    start = timer()
    size = len(dataCopy)
    mergeSort(dataCopy, 0, size - 1)
    end = timer()
    print((end - start)*1000)

    dataCopy = data
    start = timer()
    insertionSort(dataCopy)
    end = timer()
    print((end - start)*1000)

    i *= 10
