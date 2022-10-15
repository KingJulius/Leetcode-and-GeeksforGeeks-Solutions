# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def solve(root):
            if not root:
                return False
            if k-root.val in hset:
                return True
            hset.add(root.val)
            return solve(root.left) or solve(root.right)
        hset = set()
        return solve(root)
        
        