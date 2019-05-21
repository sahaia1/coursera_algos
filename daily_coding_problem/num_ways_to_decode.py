'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        mem = [-1 for _ in range(len(s))]

        def recursive(index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            if mem[index] != -1:
                return mem[index]
            if index + 1 < len(s) and (
                (int(s[index + 1]) <= 6 and int(s[index]) == 2) or
                (int(s[index]) == 1)):
                mem[index] = recursive(index + 2) + recursive(index + 1)
            else:
                mem[index] = recursive(index + 1)
            return mem[index]

        return recursive(0)