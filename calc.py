import math


def merge(x):
    return 64 * (x * (math.log(x)))
def insertion(x):
    return 8 * (x*x)

n = 0
while n < 100:
    n = n + 1
    if merge(n) > insertion(n):
        print('At ', n, ', merge is slower!')
    else:
        print('At ', n, ', insertion is slower!')

