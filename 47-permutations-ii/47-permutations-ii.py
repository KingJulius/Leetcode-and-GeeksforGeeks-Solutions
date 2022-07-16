class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        hmap = defaultdict(int)
        for i in range(len(nums)):
            hmap[nums[i]] += 1
        def solve(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in hmap:
                if hmap[i] > 0:
                    hmap[i] -= 1
                    perm.append(i)
                    solve(perm)
                    hmap[i] += 1
                    perm.pop()
        solve([])
        return res