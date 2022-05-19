class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)-1
        res = ""
        while l <= r:
            m = l + (r-l)//2
            if ord(letters[m]) <= ord(target):
                l = m + 1
            else:
                res = letters[m]
                r = m - 1
        return res if res != "" else letters[0]