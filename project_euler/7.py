import math


def is_prime(num, primes):
    limit = math.ceil(math.sqrt(num))
    for y in primes:
        if y > limit:
            break
        if num % y == 0:
            return False
    return True


def grow_prime():
    primes = [2, 3]
    i = 5
    while len(primes) != 10001:
        if is_prime(i, primes):
            primes.append(i)
        i += 2
    return primes[-1]
