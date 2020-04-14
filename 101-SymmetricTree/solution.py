# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None : return True
        return self.helper(root.left, root.right)
        
    def helper(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False

        return left.val == right.val and self.helper(left.right, right.left) and self.helper(left.left, right.right)
