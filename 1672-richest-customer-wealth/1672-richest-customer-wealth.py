class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_sum = 0
        for account in accounts:
            curr_sum = 0
            for i in range(len(account)):
                curr_sum += account[i]
            max_sum = max(curr_sum, max_sum)
        return max_sum