def func():
    sum1 = sum([x**2 for x in range(1, 101)])
    sum_of_100 = 100 * 101 // 2  # n(n+1)/2
    return sum_of_100**2 - sum1
