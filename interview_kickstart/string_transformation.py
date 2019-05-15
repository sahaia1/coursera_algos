# Complete the function below.
import os
import sys
from collections import deque, defaultdict


def is_diff_one(w1, w2):
    diff = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff += 1
            if diff > 1:
                break

    return diff == 1


def get_next_words(w, words):
    next_words = []
    word_list = list(w)
    for i, char in enumerate(word_list):
        for j in range(ord('a'), ord('z') + 1):
            if j != ord(char):
                next_char = chr(j)
            else:
                continue
            word_list[i] = next_char
            r = ''.join(word_list)
            if r in words:
                next_words.append(''.join(word_list))
        word_list[i] = char
    # print(w, next_words, words)
    return next_words


# def build_graph(words):
#     graph = defaultdict(set)
#     words = set(words)
#     for w in words:
#         word_list = list(w)
#         for i, char in enumerate(word_list):
#             for j in range(1, 26):
#                 next_char = chr(ord(char) + j)
#                 word_list[i] = next_char
#                 r = ''.join(word_list)
#                 if r in words:
#                     graph[w].add(r)
#                     graph[r].add(w)
#                 word_list[i] = char
#     return graph


def search(words, s, d):
    seen = set()
    path = []

    queue = deque()
    queue.append((s, []))

    while queue:
        n, path_so_far = queue.popleft()
        # print(n, path_so_far)
        if n not in seen:
            if n == d and len(path_so_far) >= 1:
                path = path_so_far + [n]
                break
            elif n != d:
                seen.add(n)
            for neighbours in get_next_words(n, words):
                if neighbours not in seen:
                    queue.append((neighbours, path_so_far + [n]))

    return path if len(path) >= 2 else ["-1"]


def string_transformation(words, start, stop):
    if len(start) != len(stop) or (words and len(words[0]) != len(start)):
        return ['-1']
    print(len(start), len(stop), len(words[0]))
    return search(set(words + [start, stop]), start, stop)


if __name__ == "__main__":
    f = sys.stdout

    words_size = int(input())

    words = []
    for _ in range(words_size):
        words_item = input()
        words.append(words_item)

    start = input()

    stop = input()

    res = string_transformation(words, start, stop)

    f.write('\n'.join(res))
    f.write('\n')
    f.close()
