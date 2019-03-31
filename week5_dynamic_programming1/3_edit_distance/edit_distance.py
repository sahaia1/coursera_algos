def edit_distance(word1, word2):
	D = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
	D[0] = [i for i in range(len(word2)+1)]
	for i in range(len(word1)+1):
		D[i][0] = i
	w1 = ' {}'.format(word1)
	w2 = ' {}'.format(word2)
	for i in range(1, len(word1)+1): 
		for j in range(1, len(word2)+1):
			m = []
			try:
				m.append(D[i-1][j-1] if w1[i-1] == w2[j-1] else 1 + D[i-1][j-1])
				m.append(D[i][j-1] if w1[i] == w2[j-1] else 1 + D[i][j-1])
				m.append(D[i-1][j] if w1[i-1] == w2[j] else 1 + D[i-1][j])
				D[i][j] = min(m)
			except IndexError:
				print(word1, word2, i,j)

	return D[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
