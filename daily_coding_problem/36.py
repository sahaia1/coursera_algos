'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
'''

def find_second_largest(root):
    second_max = None
    def post_order(node, count):
        nonlocal second_max
        if node:
            count = post_order(node.right, count)
            count += 1
            if count == 2:
                second_max = node.val
            count = post_order(node.left, count)
            return count
        return count
    post_order(root, 0)
    return second_max
