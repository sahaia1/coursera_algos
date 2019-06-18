'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''

def dutch_national_flag(array):
    start, end = 0, len(array)-1
    i = 0

    while i <= end:
        if array[i] == 'R':
            if i != start:
                array[i], array[start] = array[start], array[i]
                start += 1
                continue
        elif array[i] == 'B':
            if i != end:
                array[i], array[end] = array[end], array[i]
                end -= 1
                continue
        i+=1

    return array

def main():
    array =  ['B', 'R', 'G']
    print(dutch_national_flag(array))
