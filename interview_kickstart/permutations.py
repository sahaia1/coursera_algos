def is_even(i):
    return i % 2 == 0

def is_odd(i):
    return i % 2 == 1

def test_even_odd(arr, i, j):
    if i == 0 and is_even(arr[i]):
        return False
    if (is_odd(i) and is_odd(arr[i])) or (is_even(i) and is_even(arr[i])):
        return False
    if (is_odd(j) and is_odd(arr[j])) or (is_even(j) and is_even(arr[j])):
        return False
    return True


def permute(arr, i):
    if i == len(arr) - 1:
        print(''.join(list(map(str, arr))))
        return
    for j in range(i, len(arr)):
        arr[i], arr[j]  = arr[j], arr[i]
        if test_even_odd(arr, i, j):
            permute(arr, i+1)
        arr[i], arr[j]  = arr[j], arr[i]
    return

def permutations_chars(chars):
    permute(list(chars), 0)

def permutation_ints(ints):
    permute(ints, 0)