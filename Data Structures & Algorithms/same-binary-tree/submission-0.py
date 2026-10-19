# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, root, subRoot):
        
        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False

        if root.val == subRoot.val:
            left_same = self.isSameTree(root.left, subRoot.left)
            right_same = self.isSameTree(root.right, subRoot.right)

            if left_same and right_same:
                return True

        return False