# Uses python3
def edit_distance(word1, word2):
    word1 = [''] + list(word1)
    word2 = [''] + list(word2)
    D = [[0 for _ in range(len(word2))] for _ in range(len(word1))]
    D[0] = [i for i in range(len(word2))]
    for i in range(len(word1)):
        D[i][0] = i
    for i in range(1, len(word1)):
        for j in range(1, len(word2)):
            ins = D[i][j - 1] + 1
            del_ = D[i - 1][j] + 1
            match = D[i - 1][j - 1]
            mismatch = D[i - 1][j - 1] + 1
            if word1[i] == word2[j]:
                D[i][j] = min(ins, del_, match)
            else:
                D[i][j] = min(ins, del_, mismatch)
    return D[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
