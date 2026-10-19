# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root, subRoot):
        if subRoot is None:
            return True

        if root is None:
            return False

        # Check whether the trees match HERE
        if self.sameTree(root, subRoot):
            return True

        # If not, SEARCH elsewhere
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        # Check whether BOTH subtrees match
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)


