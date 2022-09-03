class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def solve(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            curr.append(candidates[i])
            solve(i, curr, total+candidates[i])
            curr.pop()
            solve(i+1, curr, total)
        solve(0, [], 0)
        return res