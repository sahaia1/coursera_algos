import math


def prime_factorization(num):
    primes = [2]

    def is_prime(x):
        for y in primes:
            if y > math.sqrt(x):
                break
            if x % y == 0:
                return False
        return True

    largest_so_far = 1

    for i in range(3, math.ceil(math.sqrt(num))):
        if is_prime(i):
            primes.append(i)
            if num % i == 0:
                largest_so_far = i
    return largest_so_far


def prime_fact2(num):
    print(num)
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            return prime_fact2(num // i)
    return num