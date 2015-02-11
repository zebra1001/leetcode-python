# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @return a ListNode

    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head
        i = 0
        while fast and i < n:
            fast = fast.next
            i += 1
        if not fast and i < n:
            return head
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
