'''
Problem # 12
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''


# Recursive Solution
def climb(N):
    def recursive(n):
        if n == 0:
            return 1
        if n == 1:
            return recursive(n - 1)
        return recursive(n - 1) + recursive(n - 2)

    return recursive(N)


def climb2(N):
    arr = [0] * (N + 1)

    arr[0] = 1
    for i in range(1, N + 1):
        if i == 1:
            arr[i] = arr[i - 1]
        else:
            arr[i] = arr[i - 1] + arr[i - 2]

    return arr[N]


def climb3(N):
    prev, curr = 1, 1

    for _ in range(2, N + 1):
        new_curr = prev + curr
        prev = curr
        curr = new_curr

    return curr