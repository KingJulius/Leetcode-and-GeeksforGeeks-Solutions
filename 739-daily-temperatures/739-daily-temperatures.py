class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Montonically Decreasing Stack...But not strictly
        stk, res = [], [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stk and stk[-1][0] < t:
                stkTemp, stkIndex = stk.pop()
                res[stkIndex] = i-stkIndex
            stk.append([t, i])
        return res