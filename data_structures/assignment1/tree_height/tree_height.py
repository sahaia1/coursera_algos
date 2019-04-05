# python3

import sys
import threading


class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, node):
        self.children.append(node)

def build_tree(n, parents):
    nodes = [Node(i) for i in range(len(parents))]
    root = None
    for i, item in enumerate(nodes):
        parent = parents[i]
        if parent == -1:
            root = item
        else:
            nodes[parent].add_child(item)

    return root

def calculate_depth(node, depth):
    if not node.children:
        return depth
    return max([calculate_depth(n, depth+1) for n in node.children])


def compute_height(n, parents):
    # Replace this code with a faster implementation
    root = build_tree(n, parents)
    return calcualte_depth(root, 0)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
