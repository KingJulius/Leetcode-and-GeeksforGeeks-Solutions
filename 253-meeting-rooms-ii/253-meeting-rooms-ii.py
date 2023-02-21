class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_list = sorted([i[0] for i in intervals])
        end_list = sorted([i[1] for i in intervals])
        count, max_count = 0, 0
        sptr, eptr = 0, 0
        
        while sptr < len(intervals):
            if start_list[sptr] < end_list[eptr]:
                count += 1
                sptr += 1
            else:
                count -= 1
                eptr += 1
            max_count = max(max_count, count)
        return max_count
        
        
        
        