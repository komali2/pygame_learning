# Consider sorting n numbers stored in array A by first finding the smallest element
# of A and exchanging it with the element in A[1]. Then find the second smallest
# element of A, and exchange it with A[2]. Continue in this manner for the first n  1
# elements of A.
# I think it means A[0]
def exchange_values(array, index1, index2):
    storage = array[index1]
    array[index1] = array[index2]
    array[index2] = storage
    return array
def my_selection_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]: 
                array = exchange_values(array, i, j)

    return array


print(my_selection_sort([5, 2, 4, 6, 1, 3]))
