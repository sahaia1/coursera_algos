def edit_distance(word1, word2):
	D = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
	D[0] = [i for i in range(len(word2)+1)]
	for i in range(len(word1)+1):
		D[i][0] = i
	for i in range(1, len(word1)+1): 
		for j in range(1, len(word2)+1):
			m = []
			m.append(D[i-1][j-1] if word1[i-1] == word2[j-1] else 1 + D[i-1][j-1])
			m.append(D[i][j-1] if word1[i] == word2[j-1] else 1 + D[i][j-1])
			m.append(D[i-1][j] if word1[i-1] == word2[j] else 1 + D[i-1][j])
			D[i][j] = min(m)

	return D[-1][-1]

def test():
	print("Ed - {}".format(edit_distance('editing', 'distance')))