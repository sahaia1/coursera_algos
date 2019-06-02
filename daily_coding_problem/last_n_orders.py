'''
Problem # 16
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
'''

# from heapq import heappush, heappop
# import sys

# heap = []
# N = int(sys.argv[1])

# def record(order_id):
#     global heap, N
#     if len(heap) == N:
#         heappop(heap)
#     heappush(heap, order_id)

# def get_last(i):
#     global heap
#     if len(heap) > 0:
#         l = [heappop(heap) for _ in range(i)]
#         retval = l[-1]
#         for e in l:
#             heappush(heap, e)
#         return retval
#     return None

# O(1) implementation using a circular buffer


class CircularBuffer:
    def __init__(self, size):
        self.arr = [None] * size
        self.idx = 0

    def record(self, order_id):
        self.arr[self.idx] = order_id
        self.idx = (self.idx + 1) % len(self.arr)

    def get_last(self, i):
        index = self.idx - i
        if index < 0:
            index = len(self.arr) + index
        return self.arr[index]