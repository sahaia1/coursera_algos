# Uses python3
import sys


def find_sets(arr, index, total, mem, blacklist):
    if index in set(blacklist):
        return 0
    key = key = '{}-{}'.format(str(index), str(total))
    if key in mem:
        return mem[key]
    if total == 0:
        return 1
    if total < 0 or index < 0:
        return 0
    if arr[index] > total:
        retval = find_sets(arr, index-1, total, mem, blacklist)
    else:
        retval = find_sets(arr, index-1, total-arr[index], mem, [index] + blacklist) + find_sets(arr, index-1, total, mem, blacklist)
    mem[key] = retval
    return retval 


def partition3(l):
    if len(l) < 3:
        return 0
    s = sum(l)
    if s % 3 != 0:
        return 0
    sum_each = s // 3
    if find_sets(l, len(l) - 1, sum_each, {}, []) >= 3:
        return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
