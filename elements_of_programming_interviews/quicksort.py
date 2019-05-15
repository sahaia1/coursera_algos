def partition(arr, low, high):
	pivot = low
	i = low
	j = high
	while j > i:
		if arr[j] < arr[pivot]:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
		else:
			j -= 1
	arr[low], arr[i] = arr[i], arr[low]
	return i

def quicksort(arr, low, high):
	if low < high:
		pivot = partition(arr, low, high)
		quicksort(arr, low, pivot-1)
		quicksort(arr, pivot+1, high)
	return arr


def test():
	import random
	from copy import deepcopy
	for _ in range(1):
		a = [random.randint(-1000, 1000) for _ in range(random.randint(100, 10000))]
		b = deepcopy(a)
		try:
			assert quicksort(a, 0, len(a) - 1) == sorted(b)
		except AssertionError:
			print(a,b)