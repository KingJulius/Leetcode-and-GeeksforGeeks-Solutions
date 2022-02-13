# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, max_val):
        if not root:
            return 0
        
        res = 1 if root.val >= max_val else 0
        res += self.preorder(root.left, max(root.val,max_val))
        res += self.preorder(root.right, max(root.val,max_val))
        return res
            
    def goodNodes(self, root: TreeNode) -> int:
        return self.preorder(root, root.val)
        
            
        