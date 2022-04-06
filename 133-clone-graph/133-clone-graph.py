"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hmap = {}
        def clone(node):
            # Clone Exists
            if node in hmap:
                return hmap[node]
            # Clone Doesn't Exist
            copy = Node(node.val)
            hmap[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
        return clone(node) if node else None
        