# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param a ListNode
    # @return a ListNode

    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy_head = ListNode(0)
        dummy_head.next = head
        p = dummy_head

        while p.next and p.next.next:
            temp = p.next.next
            p.next.next = temp.next
            temp.next = p.next
            p.next = temp
            p = p.next.next

        return dummy_head.next
