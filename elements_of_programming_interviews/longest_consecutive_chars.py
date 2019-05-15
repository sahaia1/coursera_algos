def find_longest(string):
    longest_c = None
    count = 0
    c_count = 1
    prev = None

    for c in string:
        if prev == c:
            c_count += 1
        else:
            c_count = 1
        if c_count > count:
            longest_c = c
            count = c_count
        prev = c

    return {longest_c: count}