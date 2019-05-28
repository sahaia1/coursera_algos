'''
Problem # 13

Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''

from collections import Counter


def max_window_quad(s, k):
    l, r = 0, len(s) - 1
    counter_s = Counter(s)
    all_formed = len(counter_s)
    d = counter_s.copy()
    formed = all_formed
    max_window = float('-inf')

    while l < len(s):
        while r > l:
            if formed == k:
                max_window = max(max_window, r - l + 1)
                break
            char = s[r]
            d[char] -= 1
            if d[char] == 0:
                formed -= 1
            r -= 1
        # remove the char at l from the dict
        char = s[l]
        counter_s[char] -= 1
        if counter_s[char] == 0:
            all_formed -= 1
        formed = all_formed
        d = counter_s.copy()
        l += 1
        r = len(s) - 1
    return max_window if max_window != float('-inf') else -1


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s: return 0
        set_s = set(s)
        if len(set_s) < k: return len(s)
        l, r = 0, 0
        d = {}
        formed = 0
        max_ = float('-inf')
        found = False

        while r < len(s):
            char = s[r]
            count = d.get(char, 0)
            if count == 0:
                d[char] = 1
                formed += 1
            else:
                d[char] += 1
            if formed == k:
                max_ = max(max_, r - l + 1)
            while l < r and formed > k:
                char = s[l]
                if d[char] == 1:
                    d[char] -= 1
                    formed -= 1
                else:
                    d[char] -= 1
                l += 1
            r += 1

        return max_ if found else 0
