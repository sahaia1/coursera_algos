'''
Problem # 1
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''


def twoSum(nums, target):
    d = {x: i for i, x in enumerate(nums)}

    for i, num in enumerate(nums):
        if target - num in d and i != d[target - num]:
            return [i, d[target - num]]
