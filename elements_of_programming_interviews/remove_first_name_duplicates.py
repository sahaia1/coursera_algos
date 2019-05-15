class Name(object):
    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    def __eq__(self, other):
        return self.first == other.first

    def __lt__(self, other):
        return self.first < other.first if self.first != other.first else self.last < other.last

    def __repr__(self):
        return '{} {}'.format(self.first, self.last)


def remove_first_name_duplicates(A):
    A.sort()
    B = []
    prev_name = None
    for _, name in enumerate(A):
        if prev_name:
            if name == prev_name:
                continue
            else:
                B.append('{} {}'.format(name.first, name.last))
                prev_name = name
        else:
            B.append('{} {}'.format(name.first, name.last))
            prev_name = name

    return B


import pdb


def eliminate_duplicates(A):
    A.sort()
    # pdb.set_trace()
    write_idx = 1
    for cand in A[1:]:
        if cand != A[write_idx - 1]:
            A[write_idx] = cand
            write_idx += 1
    del A[write_idx:]


def main():
    A = []
    A.append(Name('Aditya', 'Sahai'))
    A.append(Name('Aditya', 'Shankar'))
    A.append(Name('Nitin', 'Bandaru'))
    A.append(Name('Nihit', 'Bandaru'))
    A.append(Name('Nihit', 'Kapoor'))
    eliminate_duplicates(A)
    print(A)


if __name__ == "__main__":
    main()