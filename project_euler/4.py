''' Largest palindrome which is a product of two 3 digit numbers'''


# Brute Force
def is_palindrome(num):
    num = str(num)
    l, r = 0, len(num) - 1
    while l < r:
        if num[l] != num[r]:
            return False
        l += 1
        r -= 1
    return True


def largest_palindrome():
    largest = float('-inf')
    for i in range(999, 99, -1):
        for j in range(990, 99, -11):
            if is_palindrome(i * j):
                product = i * j
                if product > largest:
                    largest = product
                    print(largest, i, j)
    return largest
