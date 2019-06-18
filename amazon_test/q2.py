def minimumDistance(numRows, numColumns, area):
    # WRITE YOUR CODE HERE
    def recursion(i, j, travel_so_far, d):
        if i < 0 or i >= numRows or j < 0 or j >= numColumns:
            return float('inf')
        if area[i][j] == 0:
            return float('inf')
        if area[i][j] == 9:
            return travel_so_far
        if area[i][j] == 1:
            area[i][j] = 0
            if (i, j) in d:
                return d[(i, j)]
            else:
                min_distance = min(
                    recursion(i + 1, j, 1 + travel_so_far, d),
                    recursion(i - 1, j, 1 + travel_so_far, d),
                    recursion(i, j - 1, 1 + travel_so_far, d),
                    recursion(i, j + 1, 1 + travel_so_far, d))
                d[(i, j)] = min_distance
            area[i][j] = 1
        d.pop((i, j))
        return min_distance

    return recursion(0, 0, 0, {})
