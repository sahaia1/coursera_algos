# Uses python3
import sys

def merge(arr1, arr2):
    l = len(arr1)
    k = len(arr2)
    c = []
    i, j = 0, 0
    num_inversions = 0
    while i < l and j < k:
        if arr1[i] <= arr2[j]:
            c.append(arr1[i])
            i += 1
        else:
            c.append(arr2[j])
            j += 1
            num_inversions += l - i 
    
    c.extend(arr1[i:])
    c.extend(arr2[j:])

    return c, num_inversions

def mergeSort(arr):
    n = len(arr)
    if n == 1:
        return arr, 0
    else:
        mid = n // 2
        left, left_count = mergeSort(arr[:mid])
        right, right_count = mergeSort(arr[mid:])
        merged, count = merge(left, right)
        return merged, count + left_count + right_count

def get_number_of_inversions(a, b, left, right):
    _, number_of_inversions = mergeSort(a)
    #write your code here
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
