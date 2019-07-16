def question2():
    fibo = {1: 1, 2: 2}

    def fib(x):
        if x in fibo:
            return fibo[x]
        else:
            fibo[x] = fib(x - 1) + fib(x - 2)
            return fibo[x]

    sum_ = 0
    r = 1
    while True:
        t = fib(r)
        if t > 4000000:
            break
        if t % 2 == 0:
            sum_ += t
        r += 1
    return sum_
