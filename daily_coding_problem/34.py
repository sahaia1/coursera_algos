'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
'''

from heapq import heappush, heappop
from collections import deque

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        possible_answers = []
        def is_palindrome(start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def build_fewest_palindrome(start, end):
            nonlocal possible_answers
            moves = 0
            if start == 0:
                prefix = []
                for i in range(len(s)-1, end, -1):
                    prefix.append(s[i])
                    moves += 1
                heappush(possible_answers, (moves, ''.join(prefix) + s))
            else:
                suffix = []
                for i in range(start):
                    suffix.append(s[i])
                    moves += 1
                heappush(possible_answers, (moves, s + ''.join(suffix)))


        queue = deque()
        queue.append((0, len(s)-1))
        while queue:
            st, end = queue.popleft()
            if is_palindrome(st, end):
                build_fewest_palindrome(st, end)
            if st == 0 and end >= st:
                queue.append((st, end-1))
            if end == len(s)-1 and st <= end:
                queue.append((st+1, end))

        lex_heap = []
        min_moves = possible_answers[0][0]
        while min_moves == possible_answers[0][0]:
            heappush(lex_heap, heappop(possible_answers)[1])
        
        return lex_heap[0]


if __name__ == '__main__':
    # test cases
    a = Solution()
    print(a.shortestPalindrome('race'))
    print(a.shortestPalindrome('google'))
