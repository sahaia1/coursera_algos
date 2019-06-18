'''
Problem # 27

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''


class Solution:
    def isValid(self, brackets):
        stack = []

        def pop():
            if stack:
                return stack.pop()

        for b in brackets:
            if b in '({[':
                stack.append(b)
            elif b == ')':
                ele = pop()
                if ele != '(':
                    return False
            elif b == '}':
                ele = pop()
                if ele != '{':
                    return False
            elif b == ']':
                ele = pop()
                if ele != '[':
                    return False

        return len(stack) == 0
