'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

from heapq import heappush, heappop


def firstMissingPositive(nums):
    max_heap, min_heap, num_set = [], [], set()

    for num in nums:
        if num > 0:
            if num not in num_set:
                num_set.add(num)
                heappush(min_heap, num)
                heappush(max_heap, -1 * num)

    if not min_heap:
        return 1

    if len(max_heap) == -1 * max_heap[0]:
        return (-1 * max_heap[0]) + 1

    min_element = 1

    while min_heap:
        element = heappop(min_heap)
        if element == min_element:
            min_element += 1
        else:
            return min_element
