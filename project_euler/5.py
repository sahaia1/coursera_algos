from functools import reduce
from collections import Counter


def find_primes(num, primes, a):
    if num == 1:
        return
    for y in primes:
        if num % y == 0:
            a.append(y)
            find_primes(num // y, primes, a)
            break


def check_find_primes():
    primes_below_20 = [2, 3, 5, 7, 11, 13, 17, 19]
    for x in range(2, 21):
        array = []
        find_primes(x, primes_below_20, array)
        print(array)


def check_18():
    array = []
    primes_below_20 = [2, 3, 5, 7, 11, 13, 17, 19]
    find_primes(18, primes_below_20, array)
    print(array)


def smallest_number():
    primes_below_20 = [2, 3, 5, 7, 11, 13, 17, 19]
    d = {x: 1 for x in primes_below_20}
    for x in range(2, 21):
        primes = []
        find_primes(x, primes_below_20, primes)
        counts = Counter(primes)
        for k, v in counts.items():
            d[k] = max(d[k], v)

    product = 1
    for k, v in d.items():
        while v > 0:
            product *= k
            v -= 1
    return product
