# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, node, minimum, maximum):
        if node is None:
            return True

        if node.val <= minimum or node.val >= maximum:
            return False

        left_valid = self.dfs(node.left, minimum, node.val)
        right_valid = self.dfs(node.right, node.val, maximum)

        if left_valid and right_valid:
            return True

        return False
