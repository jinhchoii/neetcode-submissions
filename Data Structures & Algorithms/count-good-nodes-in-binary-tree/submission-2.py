# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root):
        return self.dfs(root, root.val)

    def dfs(self, node, max_so_far):
        if node is None:
            return 0

        count = 0
        
        if node.val >= max_so_far:
            count = 1

        max_so_far = max(max_so_far, node.val)

        left_count = self.dfs(node.left, max_so_far)
        right_count = self.dfs(node.right, max_so_far)

        count = count + left_count + right_count

        return count
        