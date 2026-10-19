# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        if abs(left_height - right_height) > 1:
            return False

        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)

        if left_balanced and right_balanced:
            return True

        return False


    def maxDepth(self, root):

        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)