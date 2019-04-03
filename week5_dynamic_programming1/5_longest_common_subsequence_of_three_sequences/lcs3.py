#Uses python3

import sys


def lcs3(a, b, c):
    #write your code here
    a = [0] + a
    b = [0] + b
    c = [0] + c
    D = [[[0 for _ in range(len(c))] for _ in range(len(b))]
         for _ in range(len(a))]
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            for k in range(1, len(c)):
                if a[i] == b[j] == c[k]:
                    D[i][j][k] = 1 + D[i - 1][j - 1][k - 1]
                else:
                    D[i][j][k] = max(D[i - 1][j][k], D[i][j - 1][k],
                                     D[i][j][k - 1])
    return D[-1][-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
