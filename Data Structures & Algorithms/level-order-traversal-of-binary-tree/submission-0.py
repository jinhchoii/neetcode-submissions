# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        result = []

        queue = deque()
        queue.append(root)

        while queue:    
            level = []
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(level)

        return result

        