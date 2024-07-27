class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num, sec_num = float('inf'), float('inf')
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= sec_num:
                sec_num = n
            else:
                return True
        return False