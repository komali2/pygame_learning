# What is the smallest value of n such that an algorithm whose
# running time is 100n^2 runs faster than an algorithm whose running time is 2^n
# on the same machine? 
import math

def nsqured(n):
    return 100*(n*n)
def twon(n):
    return math.pow(2, n)
def faster_or_slower(x, y):
    if x < y:
        return 'faster'
    else:
        return 'slower'

counter = 0
while (True):
    counter += 1
    print('100n^2 is ', nsqured(counter))
    print('2^n is ', twon(counter))
    print('100n^n is ', faster_or_slower(nsqured(counter), twon(counter)))
    if nsqured(counter) < twon(counter):
        print(counter)
        break



    