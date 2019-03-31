def coin_change_greedy(amt, coins):
	coins.sort(reverse=True)
	def greedy(amt):
		if amt == 0:
			return 0
		for coin in coins:
			if coin <= amt:
				return 1 + greedy(amt-coin)

	return greedy(amt)

def coin_change_dp(amt, coins):
	changes = []
	changes.append(0)  
	def dp(val):
		try:
			return changes[val]
		except IndexError:
			m = []
			for coin in coins:
				if coin <= val:
					m.append(1 + dp(val - coin))
			if m:
				return min(m)
			return amt+1

	for i in range(1, amt+1):
		changes.append(dp(i))
	return changes[amt]


def test():
	coins = [1, 8, 20]
	for i in range(100):
		u, v = coin_change_greedy(i, coins), coin_change_dp(i, coins)
		if u != v:
			print("{} - greedy - {} - dp - {}".format(i, u, v))
			break

def test1():
	coins = [5, 6, 1]
	for i in range(10):
		print("{} - {}".format(i, coin_change_dp(i, coins)))

