class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        op = []
        n = len(nums)
        def solve(ip, op, i):
            if i < 0:
                res.append(op)
                return
            solve(ip, op, i-1)
            solve(ip, op+[ip[i]], i-1)       
        solve(nums, op, n-1)
        return res