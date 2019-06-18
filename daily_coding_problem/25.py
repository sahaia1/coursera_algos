'''
Problem # 25

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
'''


# Leet code solution
class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]