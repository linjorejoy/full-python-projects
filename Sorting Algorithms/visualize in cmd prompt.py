import numpy as np


def quicksort(arr, start, end):
    if start >= end:
        return

    index = partition(arr, start, end)
    quicksort(arr, start, index-1)
    quicksort(arr, index+1, end)


def partition(arr, start, end):
    index = start
    pivotValue = arr[end]
    for i in range(start, end):
        if arr[i] < pivotValue:
            swap(arr, i, index)
            index += 1
    swap(arr, index, end)
    return index


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


array = np.random.randint(5, 100, 40)

for i in range(len(array)):
    print("*"* array[i] + str(array[i]))

input("Press any key to start sorting")

quicksort(array, 0, len(array)-1)

for i in range(len(array)):
    print("*"* array[i] + str(array[i]))

input("Press any key to exit")