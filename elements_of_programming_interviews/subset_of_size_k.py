def subset_of_size_k(string, k):
    len_string = len(string)

    def subset_k(j, index, subset_so_far):
        # import pdb
        # pdb.set_trace()
        # Base Case
        length = len(subset_so_far)
        if length == k:
            print(subset_so_far)
            return
        if len_string - index < k - length:
            return
        # General Case
        subset_k(j, index + 1, subset_so_far)
        temp = '{}{}'.format(subset_so_far, string[index])
        subset_k(j - 1, index + 1, temp)
        return

    subset_k(k, 0, '')