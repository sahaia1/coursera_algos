# Uses python3
import sys

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

def get_change(m):
    #write your code here
    return coin_change_dp(m, [1,3,4])

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
