def find_subsets(subset_so_far, index, super_set):
    # base case
    if index == len(super_set):
        print('{{{}}}'.format(','.join(list(map(str, subset_so_far)))))
        return
    # recursion
    find_subsets(subset_so_far, index + 1, super_set)
    find_subsets(subset_so_far + [super_set[index]], index + 1, super_set)
    return


def find_subsets_main(super_set):
    find_subsets([], 0, super_set)
