# Searching problem
# Input: A sequence of `n` numbers `A = [a1, 12,...,an]`` and a value `v``
# Output: An index `i` such that `v = A[i]` or the special value `null`
#   if `v1 does not appear in A
# `

def linear_search(array, value):
    return_value = None
    for i in range(len(array)):
        if array[i] == value:
            return_value = i
            break
    return return_value

print(linear_search([1, 2, 3, 4, 5, 6, 7], 24))

# Looop Invariant
# At the start of each iteration of the for loop of lines 9-12, the subarray
# A[0...len(A)] does not contain the value `v` being searched for, and therefore
# the return_value is null, unless A[n] is the value `v` being searched for,
# in which case return_value is n