def find_sets(arr, start_index, mem, total):
	key = '{}-{}'.format(str(start_index), str(total))
	if key in mem:
		return mem[key]
	if total == 0:
		return 1
	if start_index >= len(arr):
		return 0
	if total < 0:
		return 0
	if arr[start_index] > total:
		ret_val = find_sets(arr, start_index+1, mem, total)
	else:
		ret_val = find_sets(arr, start_index+1, mem, total - arr[start_index]) + find_sets(arr, start_index+1, mem, total) 
	mem[key] = ret_val
	return ret_val

def find_sets_of_16(l):
	mem = {}
	return find_sets(l, 0, mem, 16)

def test():
	print(find_sets_of_16([2,4,6,10]))
