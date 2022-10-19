class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in hmap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
            
        visit, cycle = set(), set()
        hmap = {i:[] for i in range(numCourses)}
        res = []
        
        # A course has 3 possible states
        # visited -> crs has been added to output
        # visiting -> crs not added to output,  but added to cycle
        # unvisited -> crs not added to output or cycle
        
        for crs, pre in prerequisites:
            hmap[crs].append(pre)
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
                
                