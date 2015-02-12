# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
        	return True
        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, left, right):
    	if not left and not right:
    		return True
    	if left and right and left.val == right.val:
    		return self._isSymmetric(left.left, right.right) and self._isSymmetric(left.right, right.left)
    	return False


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
        	return True
        if not root.left and not root.right:
        	return True
        if not root.left or not root.right:
        	return False

        left_stack = [root.left]
        right_stack = [root.right]

        while left_stack and right_stack:
        	left = left_stack.pop()
        	right = right_stack.pop()
        	if left.val != right.val:
        		return False

        	if (left.left and not right.right) or (left.right and not right.left):
        		return False
        	if (not left.left and right.right) or (not left.right and right.left):
        		return False

        	if left.left and right.right:
        		left_stack.append(left.left)
        		right_stack.append(right.right)
        	if left.right and right.left:
        		left_stack.append(left.right)
        		right_stack.append(right.left)
       	return True  