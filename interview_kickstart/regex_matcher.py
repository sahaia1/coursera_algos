def regex_matcher(input_, regex):
    def match_(i, j):
        # base case
        if j == len(regex):
            if i == len(input_):
                return True
            else:
                return False
        if i == len(input_):
            return match_(i, j + 1)
        # General case
        if input_[i] == regex[j]:
            return match_(i + 1, j + 1)
        elif regex[j] == '*':
            return match_(i + 1, j) or match_(i, j + 1)
        else:
            return False

    return match_(0, 0)