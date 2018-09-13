import cmath

def merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    arrayL = array[0:n1+1 ]
    arrayR = array[0:n2+1]
    for i in range(0, n1):
        arrayL[i] = array[p + i - 1]
    for j in range(0, n2):
        arrayR[j] = array[q + j]
    i = 1
    j = 1
    arrayL[n1 + 1] = cmath.inf
    arrayR[n2 + 1] = cmath.inf
    for k in range(p, r):
        if arrayL[i] <= arrayR[j]:
            array[k] = arrayL[i]
            i = i + 1
        else: 
            array[k] = arrayR[j]
            j = j + 1


print(merge([5, 2, 4, 6, 1, 3]))
