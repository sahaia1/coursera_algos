def dutch_flag_problem(arr):
	equal = 1
	pivot = 0
	smaller = 0
	high = len(arr) - 1
	while equal <= high:
		import pdb
		# pdb.set_trace()
		if arr[equal] < arr[pivot]:
			smaller += 1
			if smaller != equal:
				arr[smaller], arr[equal] = arr[equal], arr[smaller]
			else:
				equal += 1
		elif arr[equal] == arr[pivot]:
			equal += 1
		else:
			arr[equal], arr[high] = arr[high], arr[equal]
			high -= 1
	arr[smaller], arr[pivot] = arr[pivot], arr[smaller]
	print(arr, smaller, equal)

def dutch_partition_with_pivot(a, pivot):
	import pdb
	smaller, equal, larger = 0, 0, len(a)
	pi = a[pivot]
	while equal < larger:
		# pdb.set_trace()
		if a[equal] < pi:
			a[equal], a[smaller] = a[smaller], a[equal]
			equal, smaller = equal+1, smaller+1
		elif a[equal] == pi:
			equal += 1
		else:
			larger -= 1
			a[equal], a[larger] = a[larger], a[equal]
	return a
