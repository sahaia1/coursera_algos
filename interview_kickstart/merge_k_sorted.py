import heapq
import pdb
import os
import sys


def mergeArrays(A):
	'''
	Merge K Sorted arrays
	'''
	k = len(A)
	ans = []
	h = []
	lens = [len(e) for e in A]
	factor = None
	for i in range(k):
		for j in range(lens[i]-1):
			if A[i][j] > A[i][j+1]:
				factor = -1
				break
			elif A[i][j] < A[i][j+1]:
				factor = 1
				break
		if factor:
			break

	if factor == None:
		factor = 1

	# Build a heap of K size
	for i in range(k):
		heapq.heappush(h, (factor * A[i][0], i, 0))

	while len(h) > 0:
		a = heapq.heappop(h)
		ans.append(factor * a[0])
		array_idx, next_i = a[1], a[2]
		if lens[array_idx] > next_i + 1:
			heapq.heappush(h, (factor * A[array_idx][next_i+1], array_idx, next_i+1))

	return ans


if __name__ == "__main__":
    f = sys.stdout

    arr_rows = int(input())
    arr_columns = int(input())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    res = mergeArrays(arr)
    # pdb.set_trace()

    f.write('\n'.join(map(str, res)))
    f.write('\n')

    f.close()



