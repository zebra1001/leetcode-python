# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers

    def levelOrderBottom(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        result = [[root.val]]
        queue = []
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

        while queue:
            prev = queue
            queue = []
            r = []
            for node in prev:
                r.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(r)
        result.reverse()

        return result
