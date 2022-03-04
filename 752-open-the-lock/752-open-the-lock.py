class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        def children(state):
            res = []
            for i in range(4):
                digit = str((int(state[i])+1)%10)
                res.append(state[:i] + digit + state[i+1:])
                digit = str((int(state[i])-1+10)%10)
                res.append(state[:i] + digit + state[i+1:])
            return res
        
        q = deque()
        q.append(["0000", 0])
        visitSet = set(deadends)
        while q:
            state, turns = q.popleft()
            if state == target:
                return turns
            for child in children(state):
                if child not in visitSet:
                    visitSet.add(child)
                    q.append([child, turns+1])
        
        return -1
            