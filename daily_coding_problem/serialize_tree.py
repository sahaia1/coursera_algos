'''
Problem # 3
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node, level=0):
    if node:
        string = "{}({}){}({}){}".format(node.val, level,
                                         serialize(node.left,
                                                   level + 1), level,
                                         serialize(node.right, level + 1))
        return string
    return '*'


def deserialize(string, level=0):
    if string != '*':
        val, left, right = string.split('({})'.format(level))
        node = Node(val, deserialize(left, level + 1),
                    deserialize(right, level + 1))
        return node
    return None


def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'