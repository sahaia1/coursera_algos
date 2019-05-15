def paran_pairs(n):
    res = []

    def gen_pairs(k, string_so_far):
        # Base case
        if k == 0:
            res.append(string_so_far)
            return

        # General Case
        temp1 = '({})'.format(string_so_far)
        gen_pairs(k - 1, temp1)
        temp2 = '(){}'.format(string_so_far)
        gen_pairs(k - 1, temp2)
        temp3 = '{}()'.format(string_so_far)
        if temp3 != temp2:
            gen_pairs(k - 1, temp3)

    gen_pairs(n - 1, '()')
    return res


def book_sol(n):
    res = []

    def gen_pairs(left, right, string_so_far):
        if left > 0:
            gen_pairs(left - 1, right, string_so_far + '(')
        if left < right:
            gen_pairs(left, right - 1, string_so_far + ')')
        if not right:
            res.append(string_so_far)
        return

    gen_pairs(n, n, '')
    return res


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped


def main():
    import random
    import timeit
    i_win, book_wins = 0, 0
    for i in range(10):
        pairs = random.randint(1, 5)
        print('running {}th run with {} pairs'.format(i, pairs))
        wrapped = wrapper(paran_pairs, 4)
        time_my_sol = timeit.timeit(wrapped)
        wrapped = wrapper(book_sol, pairs)
        time_book_sol = timeit.timeit(wrapped)
        if time_my_sol > time_book_sol:
            i_win += 1
        else:
            book_wins += 1
    print(i_win, book_wins)
