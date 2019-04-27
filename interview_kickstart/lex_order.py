import os
import sys
#
# Complete the solve function below.
#
from collections import defaultdict

class summary:
    def __init__(self):
        self.size = 0
        self.highest = None

def solve(arr):
    #
    # Write your code here.
    #
    d = defaultdict(summary)
    
    for i, element in enumerate(arr):
        k, v = element.split()
        d[k].size += 1
        if d[k].highest and d[k].highest < v:
            d[k].highest = v
        elif d[k].highest == None:
            d[k].highest = v
    
    res = []
    for k, v in d.items():
        res.append("{}:{},{}".format(k, v.size, v.highest))

    return res

if __name__ == "__main__":
    f = sys.stdout

    arr_count = int(input())

    arr = []

    for _ in range(arr_count):
        arr_item = input()
        arr.append(arr_item)

    res = solve(arr)

    f.write('\n'.join(res))
    f.write('\n')

    f.close()