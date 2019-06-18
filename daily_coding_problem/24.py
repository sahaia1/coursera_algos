'''
Problem # 24

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
'''

# I wrote a solution which checked the parents and children,
# however, it checked each child each time and ending up having a higher complexity
# O(h + m) where m is the number of children of an arbitrary node.
# DCP blog did it better by keeping a count of number of descendants which are locked
# and updating all parents each time some node was unlocked or locked.


class BinTreeLocking:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.locked = False
        self.num_descendants_locked = 0

    def _can_be_locked_or_unlocked(self):
        if self.num_descendants_locked > 0:
            return False

        node = self.parent
        while node:
            if node.is_locked():
                return False
            node = node.parent
        return True

    def lock(self):
        if self._can_be_locked_or_unlocked():
            self.locked = True

            node = self.parent
            while node:
                node.num_descendants_locked += 1
                node = node.parent
            return True
        return False

    def unlock(self):
        if self._can_be_locked_or_unlocked():
            self.locked = False

            node = self.parent
            while node:
                node.num_descendants_locked -= 1
                node = node.parent
            return True
        return False

    def is_locked(self):
        return self.locked