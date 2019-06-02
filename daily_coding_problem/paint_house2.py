'''
Problem # 19

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
'''


class Solution:
    def minCostII(self, costs):
        if not costs: return 0
        rows, cols = len(costs), len(costs[0])
        if rows == 0 or cols == 0:
            return 0
        if rows == 1:
            return min(costs[0])


#         def recursive(house, prev_color, cost_till_now):
#             if house == rows:
#                 return cost_till_now
#             _cost = []
#             for j in range(cols):
#                 if prev_color != None and j == prev_color:
#                     continue
#                 _cost.append(recursive(house+1, j, cost_till_now + costs[house][j]))
#             return min(_cost)

#         return recursive(0, None, 0)

        min_, min_2 = float('inf'), float('inf')
        min_i, min_j = None, None

        for j in range(cols):
            if costs[rows - 1][j] < min_:
                min_, min_2 = costs[rows - 1][j], min_
                min_i, min_j = j, min_i
            elif costs[rows - 1][j] < min_2:
                min_2 = costs[rows - 1][j]
                min_j = j

        for house in range(rows - 2, -1, -1):
            new_min, new_min2 = float('inf'), float('inf')
            new_min_i, new_min_j = None, None
            for j in range(cols):
                if j != min_i:
                    costs[house][j] += min_
                else:
                    costs[house][j] += min_2
                if costs[house][j] < new_min:
                    new_min, new_min2 = costs[house][j], new_min
                    new_min_i, new_min_j = j, new_min_i
                elif costs[house][j] < new_min2:
                    new_min2 = costs[house][j]
                    new_min_j = j
            min_, min_2 = new_min, new_min2
            min_i, min_j = new_min_i, new_min_j

        return min(costs[0])