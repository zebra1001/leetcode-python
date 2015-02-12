# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    ''' SLOW '''
    def isBalanced(self, root):
    	if not root:
    		return True
    	if abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1:
    		return self.isBalanced(root.left) and self.isBalanced(root.right)
    	else:
    		return False
        

    def getHeight(self, root):
    	if not root:
    		return 0
    	return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
    	if not root:
    		return True
    	if self.getHeight(root) == -1:
    		return False
    	else:
    		return True

    def getHeight(self, root):
    	if not root:
    	   return 0

    	left_height = self.getHeight(root.left)
    	right_height = self.getHeight(root.right)

    	if left_height == -1 or right_height == -1:
    		return -1

    	if abs(left_height - right_height) <= 1:
    		return max(left_height, right_height) + 1
    	else:
    		return -1
