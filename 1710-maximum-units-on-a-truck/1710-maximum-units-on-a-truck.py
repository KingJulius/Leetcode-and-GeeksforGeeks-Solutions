class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        res = 0
        for numboxes, unit in boxTypes:
            if truckSize <= numboxes:
                res += (truckSize*unit)
                break
            res += (numboxes*unit)
            truckSize -= numboxes
        return res