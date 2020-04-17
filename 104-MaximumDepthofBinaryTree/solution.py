# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None: return 0
        bfs = [root]
        ans = 0
        nex = []
        
        while bfs:
            nex = []
            for node in bfs:
                # bfs.pop(0)
                if node.left!=None: 
                    nex.append(node.left)    
                if node.right!=None: 
                    nex.append(node.right)                
            ans += 1
            bfs = nex
           
        return ans
