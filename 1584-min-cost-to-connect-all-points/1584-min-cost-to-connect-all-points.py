import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d = {i:{} for i in range(len(points))}
        
        i, j = 0, 1
        while j < len(points) and i < j:
            node1 = points[i]
            node2 = points[j]
            dist = abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])
            d[i][j] = dist
            d[j][i] = dist
            j += 1
            if j == len(points):
                i += 1
                j = i + 1
                     
        visitSet = set()
        min_heap = [[0, 0]]
        cost = 0

        while min_heap:
            di, po = heappop(min_heap)
            # Duplicates being added to min heap
            if po in visitSet:
                continue
            cost += di
            visitSet.add(po)
            neighbs = d[po]
            for neigh in neighbs:
                if neigh not in visitSet:
                    new_cost = neighbs[neigh]
                    heappush(min_heap, [new_cost, neigh])
                
        
        return cost