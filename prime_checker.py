# Check if something is prime

def prime_checker(n):
    if n < 1:
        return False
    elif n<= 3:
        return True
    elif n % 3 == 0 or n % 2 == 0:
        return False
    i = 5
    while i * i < n:
        # There's somet fancy thing you can add here to do like
        # 6k+3 but I don't understand it yet so I didn't add it
        # this works because you only need to check divisors
        # smaller than sqrt(n)
        # Checking bigger than that is redundant
        if i % n == 0:
            return False
        i = i + 1
    return True

for x in [5, 7, 17, 11]:
    print(prime_checker(x))



