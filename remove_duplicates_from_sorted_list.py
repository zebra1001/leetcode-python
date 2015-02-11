# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def deleteDuplicates(self, head):
        if not head:
            return head
        fast = head
        slow = head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = fast
            fast = fast.next
        slow.next = fast
        return head
