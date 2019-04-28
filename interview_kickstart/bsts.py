def permutations(n):
    len_l = n
    l = list(range(1, n+1))
    def permute(index):
        # Base case
        if index == len_l:
            print(''.join(list(map(str,l))))

        # general case
        for i in range(index, len_l):
            l[i], l[index] = l[index], l[i]
            permute(i+1)
            l[i], l[index] = l[index], l[i]

    
    permute(0)
