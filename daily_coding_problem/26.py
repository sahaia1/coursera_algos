'''
Problem # 26

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        if not head or n == 0: return head
        node = head
        n_node = head
        prev = None
        count = 0

        while node:
            if count >= n:
                prev = n_node
                n_node = n_node.next
            node = node.next
            count += 1

        if n_node == head:
            head = head.next
        else:
            prev.next = n_node.next

        return head