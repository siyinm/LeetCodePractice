# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        trav = self.inorderTraversal(root)
        for i in range(len(trav)-1):
            if trav[i]>=trav[i+1]:
                return False
        return True

    def inorderTraversal(self, root: TreeNode) -> List[int]: 
        stack, ret = [], []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ret.append(cur.val)
                cur = cur.right
        return ret
class Solution2:

    def isValidBST(self, root: TreeNode) -> bool:
        def ds(root,mi,ma):
            if root==None:
                return True
            if root.val<=mi or root.val>=ma:
                return False
            return ds(root.left,mi,root.val)&ds(root.right,root.val,ma)
        return ds(root,float("-inf"), float("inf"))

