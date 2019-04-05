# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, n in enumerate(text):
        if n in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(n)

        if n in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack:
                b = opening_brackets_stack.pop()
            else:
                return False, i
            if not are_matching(b,n):
                return False, i
    l = len(opening_brackets_stack)
    if l > 0:
        return False, 0
    return True, 0



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch[0]:
        print("Success")
    else:
        print(mismatch[1]+1)

if __name__ == "__main__":
    main()
