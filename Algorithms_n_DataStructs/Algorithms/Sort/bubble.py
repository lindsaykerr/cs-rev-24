# Bubble sort is a naive linear sorting algorithm, with a worst and average
# order of magnitude of O(n^2), can be used to sort a small number of items

def sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
