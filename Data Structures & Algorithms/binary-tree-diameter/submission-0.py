# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        self.maxDepth(root)

        return self.diameter

    def maxDepth(self, root):
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        current_diameter = left_depth + right_depth

        self.diameter = max(self.diameter, current_diameter)

        return 1 + max(left_depth, right_depth)