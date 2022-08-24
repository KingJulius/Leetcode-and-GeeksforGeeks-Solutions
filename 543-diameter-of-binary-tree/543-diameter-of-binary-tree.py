# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            tmp = 1 + max(l, r)
            ans = max(tmp, 1+l+r)
            res[0] = max(res[0], ans)
            return tmp
        res = [0]
        dfs(root)
        return res[0]-1