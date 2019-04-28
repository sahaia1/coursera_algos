def printArray(s, j):
    print('{{{}}}'.format(','.join(s[:j])))

def subset(a, i, s, j):
    if i == len(a):
        printArray(s, j)
        return
    subset(a, i+1, s, j)
    s[j] = a[i]
    subset(a, i+1, s, j+1)
    return

def main(arr):
    subset(arr, 0, [None] * len(arr), 0)