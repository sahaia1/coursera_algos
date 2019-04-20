import os
import sys

# Complete the function below.
import heapq
import pdb


def topK(arr, k):
    s = set()
    h = []
    
    # pdb.set_trace()
    
    for j in range(len(arr)):
        if arr[j] not in s:
            if len(h) < k:
                heapq.heappush(h, arr[j])
                s.add(arr[j])
            elif arr[j] > h[0]:
                heapq.heappushpop(h, arr[j])
                s.add(arr[j])
    
    return h


if __name__ == "__main__":
    f = sys.stdout

    arr_cnt = 0
    arr_cnt = int(input())
    arr_i = 0
    arr = []
    while arr_i < arr_cnt:
        arr_item = int(input())
        arr.append(arr_item)
        arr_i += 1


    k = int(input())

    res = topK(arr, k);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )


    f.close()
