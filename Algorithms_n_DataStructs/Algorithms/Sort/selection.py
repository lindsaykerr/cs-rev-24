
def sort(arr):
    for i in range(len(arr)-1, -1, -1):
        maxIndx = i
        for j in range(0, i):
            if arr[j] > arr[maxIndx]:
                maxIndx = j

        if maxIndx != i:
            temp = arr[i]
            arr[i] = arr[maxIndx]
            arr[maxIndx] = temp

