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


# Merge Sort - O(n log n) time, O(n) space
# Recursively splits the array in half, then merges the sorted halves back together
# The merge step compares front elements of each half and builds a sorted result
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# Quick Sort - O(n log n) avg / O(n^2) worst time, O(log n) space
# Picks a pivot, partitions elements into less-than and greater-than groups, recurses on each
# Last element is used as pivot; partition walks left pointer until it exceeds right
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = _partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

    return arr


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
