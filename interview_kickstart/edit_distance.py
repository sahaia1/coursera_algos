def edit_distance(str1, str2):
    def count_steps(i, j):
        # Base Case
        if i == len(str1):
            return len(str2) - j
        if j == len(str2):
            return len(str1) - i

        # General Case
        if str1[i] == str2[j]:
            return count_steps(i + 1, j + 1)
        else:
            return 1 + min(
                count_steps(i + 1, j), count_steps(i, j + 1),
                count_steps(i + 1, j + 1))

    return count_steps(0, 0)