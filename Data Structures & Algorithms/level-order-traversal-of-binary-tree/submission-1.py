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


# create a list to put the final result
# create a queue and add the initial node on the queue
# create a while loop, while queue: to make it keep running until queue becomes empty
# in the while loop, create a list to store the values to contain the items for that level
# make a for loop that runs for len(queue), create variable node to store the node to pop, and then append the value of the node on the level list, check if node has any node.left or node.right and add to queue if there is
# add the level list as one item onto final result list
# return result outside the while loop
        