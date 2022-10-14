# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        res = []
        while q:
            qLen = len(q)
            lvl = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if lvl:
                s = 0
                for k in lvl:
                    s += k
                res.append(s/len(lvl))
        return res