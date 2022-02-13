# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(curr, num):
            if not curr:
                return 0
            num = num * 10 + curr.val
            if not curr.left and not curr.right:
                return num
            l = helper(curr.left, num)
            r = helper(curr.right, num)
            return l + r
        return helper(root, 0)
           