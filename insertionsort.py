from generate import read
import time

def insertionSort(arr):
    global length, list
    
    # iterate over the array from the second element to the last
    for i in range(1, length):
        
        # store the current element in a temporary variable
        temp = list[i]
        
        # iterate over the sorted part of the array to find the correct position for the current element
        j = i-1
        while j >= 0 and list[j] > temp:
            list[j+1] = list[j] # shift elements to the right
            j -= 1
        
        # insert the current element into its correct position
        list[j+1] = temp


# Print the insertion sort function's results the same way as in quicksort.py
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