# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        length_of_A = 0
        tailA = headA
        while tailA:
        	tailA = tailA.next
        	length_of_A += 1

        length_of_B = 0
        tailB = headB
        while tailB:
        	tailB = tailB.next
        	length_of_B += 1
        
        diff = abs(length_of_A - length_of_B)
        if length_of_A > length_of_B:
        	while diff > 0:
        		headA = headA.next
        		diff -= 1
        elif length_of_A < length_of_B:
        	while diff > 0:
        		headB = headB.next
        		diff -= 1

        while headA and headB:
        	if headA.val == headB.val:
        		return headA
        	else:
        		headA = headA.next
        		headB = headB.next

        return None