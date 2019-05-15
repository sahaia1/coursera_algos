def intersection(a, b):
	# Brute Force Solution to find the intersection
	# set of two sorted arrays
	c = []
	for each in a:
		if each not in c:
			for i in range(len(b)):
				if b[i] == each:
					c.append(each)
					break

	return c

def intersection2(a, b):
	i, j = 0, 0
	c = []
	len_a, len_b = len(a), len(b)
	prev_a, prev_b = None, None

	while i < len_a and j < len_b:
		if a[i] < b[j]:
			prev_a = a[i]
		elif b[j] < a[i]:
			prev_b = b[j]
		else:
			c.append(a[i])
			prev_a, prev_b = a[i], a[i]
		while i < len_a and a[i] == prev_a:
			i += 1
		while j < len_b and b[j] == prev_b:
			j += 1

	return c




def test():
	a = [2,3,3,5,5,6,7,7,8,12]
	b = [5,5,6,8,8,9,10,10]
	print(intersection(a,b))
	print(intersection2(a,b))