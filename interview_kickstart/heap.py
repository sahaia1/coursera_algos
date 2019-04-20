'''
Heap class
'''

class Heap(object):
	def __init__(self, arr, max=False):
		self.factor = -1 if max else 1
		self.arr = arr
		self.size = len(arr)
		self.build_heap()

	def build_heap(self):
		for i in range(self.size//2 - 1, -1, -1):
			self.heapify_down(i)

	def heapify_down(self, idx):
		to_swap = idx
		left_child = self.get_left(idx)
		right_child = self.get_right(idx)

		if left_child and self.factor * self.arr[left_child] < self.factor * self.arr[to_swap]:
			to_swap = left_child

		if right_child and self.factor * self.arr[right_child] < self.factor * self.arr[to_swap]:
			to_swap = right_child

		if to_swap != idx:
			self.swap(to_swap, idx)
			self.heapify_down(to_swap)

	def get_left(self, idx):
		left_child = 2 * idx + 1
		return left_child if left_child < self.size else None

	def get_right(self, idx):
		right_child = 2 * idx + 2
		return right_child if right_child < self.size else None

	def swap(self, i, j):
		self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

	def heap_sort(self):
		n = self.size

		while self.size > 0:
			self.swap(0, self.size-1)
			self.size -= 1
			self.heapify_down(0)

		self.size = n
		return list(reversed(self.arr))


if __name__ == '__main__':
	arr = [1,23,123,123223,0,-123,-1423534,2]
	h = Heap(arr[:], max=True)
	assert h.heap_sort() == sorted(arr, reverse=True)
	print(h.arr)
