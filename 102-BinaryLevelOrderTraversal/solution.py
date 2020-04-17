# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None: return []
        bfs = [root]
        ans = []
        nex = []
        
        while bfs:
            nex = []
            temp = []
            for node in bfs:
                # bfs.pop(0)
                temp.append(node.val)
                if node.left!=None: 
                    nex.append(node.left)
                    
                if node.right!=None: 
                    nex.append(node.right)                
            ans.append(temp)
            bfs = nex
            
           
        return ans



