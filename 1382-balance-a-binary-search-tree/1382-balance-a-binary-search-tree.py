# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        def createBalancedBST(l, r):
            if l <= r:
                m = l + (r-l)//2
                node = TreeNode(res[m])
                node.left = createBalancedBST(l, m-1)
                node.right = createBalancedBST(m+1, r)
                return node   
        res = []
        inorder(root)
        newRoot = createBalancedBST(0, len(res)-1)
        return newRoot