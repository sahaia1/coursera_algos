'''
Problem # 20
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        a = headA
        b = headB
        lastA = None
        lastB = None
        while True:
            if a == b:
                return a
            if lastA != None and lastB != None and lastA != lastB:
                return None
            if a.next:
                a = a.next
            else:
                lastA = a
                a = headB
            if b.next:
                b = b.next
            else:
                lastB = b
                b = headA