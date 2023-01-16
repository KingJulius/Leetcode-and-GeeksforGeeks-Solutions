class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start < res[-1][1]:
                return False
            else:
                res.append([start, end])
        return True