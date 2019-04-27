# Find the number of ways to climb N stairs given a list of valid number of strides you can take
def find_num_ways(steps, stairs):
    def climb(stairs_left):
        # Base case
        if stairs_left == 0:
            return 1
        if stairs_left < 0:
            return 0
        return sum([climb(stairs_left - step) for step in steps])

    return climb(stairs)
