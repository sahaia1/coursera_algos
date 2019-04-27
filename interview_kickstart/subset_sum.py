def subset_sum(sum_left, index, array, array_len):
    if sum_left == 0:
        return 1
    if sum_left < 0 or index == array_len:
        return 0
    return subset_sum(sum_left, index + 1, array, array_len) + subset_sum(
        sum_left - array[index], index + 1, array, array_len)


def subset_sum_main(sum_total, array):
    return subset_sum(sum_total, 0, array, len(array)) if sum_total > 0 else 0


def main():
    super_set = [1, 2, 3, 4, 5, 6]
    sum_left = 8
    print(subset_sum_main(sum_left, super_set))