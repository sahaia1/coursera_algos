import random

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
            num_inversions += 1
    
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

if __name__ == "__main__":
    pass
    # for _ in range(10000):
    #     l = []
    #     length = random.randint(1, 10000)
    #     for _ in range(length):
    #         l.append(random.randint(-100000, 1000000))
    #     # check sorting
    #     assert mergeSort(l) == sorted(l)