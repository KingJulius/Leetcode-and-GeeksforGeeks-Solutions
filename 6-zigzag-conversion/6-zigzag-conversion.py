class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        new_s = ""
        for i in range(numRows):
            for j in range(i, len(s), (numRows-1)*2):
                # Common Column Value
                new_s += s[j]
                # Uncommon Column Value
                if i>0 and i<numRows-1 and j+(numRows-1)*2-2*i < len(s):
                    new_s += s[j + (numRows-1)*2-2*i]
        return new_s