from bisect import bisect_left


def binsearch(arr, k):
    pos = bisect_left(arr, k)
    return pos if pos != len(arr) and arr[pos] == k else None


def three_sum(arr):
    arr.sort()
    res = set()

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            sum_ = arr[i] + arr[j]
            k = binsearch(arr, -1 * sum_)
            if k != None and k != i and k != j:
                to_add = '{},{},{}'.format(*sorted([arr[i], arr[j], arr[k]]))
                res.add(to_add)
    

    return list(res)
