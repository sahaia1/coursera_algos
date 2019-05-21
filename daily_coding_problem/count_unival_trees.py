'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 '''

## Leet code problem - 250

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        count = 0

        def recursive(node, parent):
            nonlocal count
            if node:
                retval = False
                if parent and node.val == parent.val:
                    retval = True
                left = recursive(node.left, node)
                right = recursive(node.right, node)
                if left and right:
                    count += 1
                return retval and left and right
            return True

        recursive(root, None)
        return count
