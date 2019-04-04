# Uses python3
import sys


def ks(W, items):
    D = [[0 for _ in range(W + 1)] for _ in range(len(items) + 1)]
    for i, item in enumerate(items, start=1):
        for j in range(1, W + 1):
            D[i][j] = D[i - 1][j]
            if item <= j:
                if D[i - 1][j - item] + item > D[i][j]:
                    D[i][j] = D[i - 1][j - item] + item

    return D[-1][-1]


def optimal_weight(W, w):
    # write your code here
    return ks(W, w)


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
