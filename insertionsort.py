# Insertion sort implementation for sorting arrays of numbers

def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        # insert array[j] into the sorted sequence array[1..j-1].
        i = j
        while (i > 0) and (array[i-1] > key):
            array[i] = array[i-1]
            i = i - 1
        array[i] = key
    return array

print(insertion_sort([5, 2, 4, 6, 1, 3]))