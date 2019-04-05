# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

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

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                root = build_tree(self.n, self.parent)
                return calculate_depth(root, 1)

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
