from generate import read
import time
import random
import sys

# Set bigger recursion limit to avoid running into errors
# when running it on larger datasets
sys.setrecursionlimit(150000)

# Function to sort the array using median quicksort algorithm
def medianQuicksort(arr, left, right):
    # Check if left is greater than or equal to right
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

# Function to sort the array using iterative quicksort algorithm
def iterativeQuicksort(arr):
    # Initialize start and end pointers
    start = 0
    end = len(arr) - 1
    
    # Iterate until the array is fully sorted
    while start < end:
        # Choose a random pivot
        pivot = random.choice(arr)
        i = start
        j = end
        
        # Partition the array around the pivot element
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        # Determine which subarray to sort next
        # by simulating recursive calls using a stack
        if j - start < end - i:
            stack_top = end
            end = j
            j = stack_top
        else:
            stack_top = start
            start = i
            i = stack_top
    
    return arr

# Function to sort the array using recursive quicksort algorithm
def recursiveQuicksort(arr):
    # Check if array has only one element
    if len(arr) <= 1:
        return arr

    # Choose a random pivot
    pivot = random.choice(arr)
    left = []
    right = []

    # Partition the array into two sub-arrays
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    # Sort the two sub-arrays recursively and return the sorted array
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
    # Choose the first element as pivot
    pivot_element = list[left]
    # Initialise lower and upper bounds
    lb = left
    ub = right
    # Partition the array into two sub-arrays
    while left < right:
        while list[left] <= pivot_element:
            left += 1
        while list[right] > pivot_element:
            right -= 1
        if left < right:
            # Swap elements at 'left' and 'right'
            list[left], list[right] = list[right], list[left]
    # Place the pivot element at its correct position
    list[lb] = list[right]
    list[right] = pivot_element
    # Return the position of the pivot element
    return right
 
def quickSort(left, right):
    if left < right:
        pivot = partition(left, right)
        # Sort the left and right sub-arrays recursively
        quickSort(left, pivot-1)
        quickSort(pivot+1, right)

for i in range(0,5):
    # Set initial array length and maximum length for the array
    length = 1
    max_length = 100000
    # Run the loop until maximum length is reached
    while length <= max_length:
        # Print the current array length
        print(f"\nLength\t: {length}")
        # Read in the array from user input
        list = read()
        # Select which sorting algorithm to use based on i value and
        # record the start time, end time, and print time taken for each
        if i == 0:
            t1 = time.perf_counter()
            # Call recursive quicksort function
            recursiveQuicksort(list)
            t2 = time.perf_counter()
            print(f"Recursive Quick Sort\t: {t2-t1:.6f} sec")
        elif i == 1:
            t1 = time.perf_counter()
            # Call iterative quicksort function
            iterativeQuicksort(list)
            t2 = time.perf_counter()
            print(f"Iterative Quick Sort\t: {t2-t1:.6f} sec")
        elif i == 2:
            t1 = time.perf_counter()
            # Call median quicksort function
            medianQuicksort(list, 0, length - 1)
            t2 = time.perf_counter()
            print(f"Median Quick Sort\t: {t2-t1:.6f} sec")
        elif i == 3:
            t1 = time.perf_counter()
            # Call partition quicksort function
            quickSort(0, length - 1)
            t2 = time.perf_counter()
            print(f"Partition Quick Sort\t: {t2-t1:.6f} sec")
        else:
            t1 = time.perf_counter()
            # Call stack quicksort function
            stackQuicksort(list)
            t2 = time.perf_counter()
            print(f"Stack Quick Sort\t: {t2-t1:.6f} sec")
        # Increase array length depending on case
        if(length<10):
            length = length + 1
        else:
            length = length * 10

