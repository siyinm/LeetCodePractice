Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        if n<1: return []
        from collections import defaultdict
        trees = defaultdict(list)
        
    
        def helper(start, end):
            if start > end:
                return [None]
            if end == start:
                return [TreeNode(start)]
            if (start, end) in trees:
                return trees[(start, end)]
            for val in range(start, end+1):
                for left in helper(start, val-1):
                    for right in helper(val+1, end):
                        root = TreeNode(val)
                        root.left = left
                        root.right = right
                        trees[(start, end)].append(root)
            return trees[(start, end)]
        return helper(1, n)
             
            
            
