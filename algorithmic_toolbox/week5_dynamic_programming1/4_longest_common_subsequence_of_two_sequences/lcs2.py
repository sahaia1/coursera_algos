#Uses python3

import sys


def lcs2(a, b):
    a = [0] + a
    b = [0] + b
    D = [[0 for _ in range(len(b))] for _ in range(len(a))]
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j]:
                D[i][j] = 1 + D[i - 1][j - 1]
            else:
                D[i][j] = max(D[i - 1][j], D[i][j - 1])
    return D[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
