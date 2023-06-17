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


# arr = np.random.randint(1, 1000, 1000)
# print(arr)
# quicksort(arr, 0, len(arr)-1)
# print("*" * 50)
# print(arr)
