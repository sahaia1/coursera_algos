'''
Problem # 9
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''


def greatest_non_adjacent_sum(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1])

    for i in range(len(arr) - 3, -1, -1):
        if i + 3 >= len(arr):
            arr[i] = arr[i] + arr[i + 2]
        else:
            arr[i] = arr[i] + max(arr[i + 2], arr[i + 3])

    return max(arr[0], arr[1])