# Insertion sort is another naive sorting algorithm with a worst case order of
# magnitude of n^2

# One of the cons about insertion sort is that does not maintain the exact
# order exact values. I most cases this is not an issue it only becomes an
# issue when the value in the array represents some the key/id of an object,
# if two objects share the same id but have different values then this could
# cause unwanted results

def sort(arr):
    # set the index of the sort partition
    parIndx = 0

    # when the partition index is the same as the array then arr will be sorted
    while parIndx < len(arr):
        # store the value found at the partition index
        parval = arr[parIndx]
        # set a decrementer that will be used to iterate to through the
        # partition
        pos = parIndx - 1
        # loop throught the partition swapping the larger value at the
        # partition index for smaller ones within the partition
        while pos > -1 and arr[pos] > parval:
            arr[pos+1] = arr[pos]
            arr[pos] = parval
            pos -= 1

        parIndx += 1
