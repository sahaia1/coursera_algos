'''
Problem # 22
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''


class RecursiveSolution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)

        arr = [[-1 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]

        def recursive(left, right):
            if right == len(s):
                return s[left:right] in wordSet
            if arr[left][right] != -1:
                return arr[left][right]
            else:
                if s[left:right] in wordSet:
                    arr[right][right + 1] = recursive(right, right + 1)
                    arr[left][right + 1] = recursive(left, right + 1)
                    return arr[right][right + 1] or arr[left][right + 1]
                else:
                    arr[left][right + 1] = recursive(left, right + 1)
                    return arr[left][right + 1]

        return recursive(0, 1)


class IterativeSolution:
    def word_break(self, s, wordDict):
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]

    def wordBreak(self, s, wordDict):
        return self.word_break(s, set(wordDict))
