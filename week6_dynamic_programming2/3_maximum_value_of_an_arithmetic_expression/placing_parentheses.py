# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def min_and_max(nums, ops, i, j, M, m):
    min_ = float('inf')
    max_ = -float('inf')
    for k in range(i, j):
        # import pdb
        # pdb.set_trace()
        a = evalt(M[i][k], M[k + 1][j], ops[k])
        b = evalt(M[i][k], m[k + 1][j], ops[k])
        c = evalt(m[i][k], M[k + 1][j], ops[k])
        d = evalt(m[i][k], m[k + 1][j], ops[k])
        min_ = min(min_, a, b, c, d)
        max_ = max(max_, a, b, c, d)
    return (min_, max_)


def split_numbers_ops(string):
    isNumber = False
    nums = []
    ops = []
    number = 0
    for e in string:
        try:
            if isNumber:
                number = number * 10 + int(e)
            else:
                isNumber = True
                number = int(e)
        except ValueError:
            nums.append(number)
            ops.append(e)
            number = 0
            isNumber = False
    nums.append(number)

    return nums, ops


def get_maximum_value(dataset):
    #write your code here
    nums, ops = split_numbers_ops(dataset)
    n = len(nums)
    M = [[0 for _ in range(n)] for _ in range(n)]
    m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        M[i][i] = nums[i]
        m[i][i] = nums[i]

    for s in range(n):
        for i in range(n - s):
            j = i + s
            if j > i:
                m[i][j], M[i][j] = min_and_max(nums, ops, i, j, M, m)

    return M[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
