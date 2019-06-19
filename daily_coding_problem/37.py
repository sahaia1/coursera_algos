'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
'''

def print_power_set(array):
    def recursive(index, set_so_far):
        if index == len(array):
            print(set_so_far)
        else:
            recursive(index+1, set_so_far + [array[index]])
            recursive(index+1, set_so_far)


    recursive(0, [])
