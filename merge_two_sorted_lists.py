# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode

    def mergeTwoLists(self, l1, l2):
        l1 = l1
        l2 = l2

        dummy_head = ListNode(1)
        pointer = dummy_head

        while l1 and l2:
            if l1.val <= l2.val:
                pointer.next = ListNode(l1.val)
                l1 = l1.next
            else:
                pointer.next = ListNode(l2.val)
                l2 = l2.next
            pointer = pointer.next

        while l1:
            pointer.next = ListNode(l1.val)
            pointer = pointer.next
            l1 = l1.next

        while l2:
            pointer.next = ListNode(l2.val)
            pointer = pointer.next
            l2 = l2.next

        return dummy_head.next
