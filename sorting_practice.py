# Bubble Sort - O(n^2) time, O(1) space
# Each pass bubbles the largest unsorted element to the end
# i tracks passes, j walks adjacent pairs up to the already-sorted portion
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Selection Sort - O(n^2) time, O(1) space
# Each pass finds the minimum in the unsorted portion and swaps it into position
# i marks the boundary, tmp tracks the index of the current minimum
def selection_sort(arr):
    for i in range(len(arr)):
        tmp = i
        for j in range(i + 1, len(arr)):
            if arr[tmp] > arr[j]:
                tmp = j
        arr[tmp], arr[i] = arr[i], arr[tmp]
    return arr


# Insertion Sort - O(n^2) time, O(1) space
# Builds sorted portion on the left by inserting each element into its correct position
# key saves the current element, j walks left shifting larger elements right until key fits
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    pass


def quick_sort(arr):
    pass
