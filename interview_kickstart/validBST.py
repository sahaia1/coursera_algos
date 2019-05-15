import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(root: TreeNode) -> bool:
    q = collections.deque()
    q.append((root, float('-inf'), float('inf')))
    import pdb
    # pdb.set_trace()
    while q:
        f, lower, upper = q.popleft()
        if f:
            if not lower < f.val < upper:
                return False
            else:
                q.append((f.left, lower, f.val))
                q.append((f.right, f.val, upper))
    return True
