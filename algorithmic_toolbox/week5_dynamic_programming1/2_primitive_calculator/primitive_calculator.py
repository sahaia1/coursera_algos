# Uses python3
import sys

def dp(n):
    D = [-1,0]
    ans = [1]
    for i in range(2, n+1):
        m = []
        if i - 1 >= 1:
            m.append((i-1, 1 + D[i-1]))
        if i % 2 == 0 and i // 2 >= 1:
            m.append((i//2, 1 + D[i//2]))
        if i % 3 == 0 and i // 3 >= 1:
            m.append((i//3, 1 + D[i//3]))             
        a = min(m, key=lambda x: x[1])
        D.append(a[1])
        ans.append(a[0])
    sequence = [n]
    j = n - 1
    while j != 0:
        sequence.append(ans[j])
        j = ans[j] - 1
    return reversed(sequence)

def optimal_sequence(n):
    return dp(n)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
     print(x, end=' ')
