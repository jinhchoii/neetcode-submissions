# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         values = []

#         def dfs(node):
#             if node is None:
#                 return 

#             dfs(node.left)
#             values.append(node.val)
#             dfs(node.right)

#         dfs(root)
#         return values[k-1]


class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.answer = None

        self.dfs(root, k)

        return self.answer

    def dfs(self, node, k):
        if node is None:
            return

        if self.answer is not None:
            return

        self.dfs(node.left, k)

        if self.answer is not None:
            return

        self.count += 1

        if self.count == k:
            self.answer = node.val
            return

        self.dfs(node.right, k)
