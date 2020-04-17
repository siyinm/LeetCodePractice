# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None: return []
        bfs = [root]
        ans = []
        nex = []
        flag = 1
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
            if flag == 1:
                ans.append(temp)
            else:
                ans.append(temp[::-1])
            flag *= -1
            bfs = nex
            
           
        return ans
