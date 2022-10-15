class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        tsum = symbol_map[s[-1]]
        prev = s[-1]
        for i in range(len(s)-2, -1, -1):
            if symbol_map[s[i]] >= symbol_map[prev]:
                tsum += symbol_map[s[i]]
            else:
                tsum -= symbol_map[s[i]]
            prev = s[i]
        return tsum
            