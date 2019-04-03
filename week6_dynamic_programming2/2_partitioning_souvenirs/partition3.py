# Uses python3
import sys
import itertools
from collections import defaultdict


def tuple_to_string(a):
    return '.'.join([str(t) for t in a])


def partition3(A):
    D = {}
    space = [
        tuple_to_string(r) for r in itertools.combinations(range(3), len(A))
    ]
    print(space, len(space))
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
