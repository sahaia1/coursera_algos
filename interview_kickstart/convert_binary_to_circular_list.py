import sys
from collections import deque
sys.setrecursionlimit(100000 + 1000)


class TreeNode():
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr


class BinaryTree():
    class Edge():
        def __init__(self,
                     parentNodeIndex=None,
                     childNodeIndex=None,
                     leftRightFlag=None):
            self.BinaryTree = BinaryTree
            self.parentNodeIndex = parentNodeIndex
            self.childNodeIndex = childNodeIndex
            self.leftRightFlag = leftRightFlag

    def __init__(self):
        self.root = None
        self.noOfNodes = 0
        self.noOfEdges = 0
        self.rootIndex = -1
        self.nodeValues = []
        self.edges = []

    def readRawValues(self):
        self.noOfNodes = int(input())
        if self.noOfNodes > 0:
            nodeValueString = input().split(' ')
            for val in nodeValueString:
                self.nodeValues.append(int(val))

        self.rootIndex = int(input())
        self.noOfEdges = int(input())
        for i in range(self.noOfEdges):
            edgeInput = input().split(' ')
            self.edges.append(
                self.Edge(int(edgeInput[0]), int(edgeInput[1]), edgeInput[2]))

    def buildFormRawValues(self):
        if self.noOfNodes == 0:
            root = None
            return
        nodes = []
        for i in range(self.noOfNodes):
            nodes.append(TreeNode(self.nodeValues[i]))

        for i in range(self.noOfEdges):
            if self.edges[i].leftRightFlag == "L":
                nodes[self.edges[i].parentNodeIndex].left_ptr = nodes[
                    self.edges[i].childNodeIndex]
            else:
                nodes[self.edges[i].parentNodeIndex].right_ptr = nodes[
                    self.edges[i].childNodeIndex]

        self.root = nodes[self.rootIndex]


def readBinaryTree():
    inputBinaryTree = BinaryTree()
    inputBinaryTree.readRawValues()
    inputBinaryTree.buildFormRawValues()
    return inputBinaryTree.root


def printCircularList(circularListHead):
    if circularListHead == None:
        print()
        return
    tmpHead = circularListHead
    while tmpHead.right_ptr != circularListHead:
        print(tmpHead.val, end=' ')
        tmpHead = tmpHead.right_ptr
    print(tmpHead.val)


# complete the function below
def prettyPrintTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right_ptr:
        prettyPrintTree(node.right_ptr,
                        prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left_ptr:
        prettyPrintTree(node.left_ptr, prefix + ("    " if isLeft else "│   "),
                        True)


def BTtoLL(root):
    # prettyPrintTree(root)
    head, tail, prev = None, None, None

    def in_order(node, head, tail, prev):
        if node:
            head, tail, prev = in_order(node.left_ptr, head, tail, prev)
            if prev:
                prev.right_ptr = node
                node.left_ptr = prev
            prev = node
            if not head:
                head = node
            tail = node
            head, tail, prev = in_order(node.right_ptr, head, tail, prev)
            return head, tail, prev
        return head, tail, prev

    head, tail, _ = in_order(root, head, tail, prev)
    head.left_ptr = tail
    tail.right_ptr = head
    return head


def main():
    root = readBinaryTree()
    result = BTtoLL(root)
    printCircularList(result)


main()