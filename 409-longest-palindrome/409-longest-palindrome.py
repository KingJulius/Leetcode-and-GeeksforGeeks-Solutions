class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap = defaultdict(int)
        for c in s:
            hmap[c] += 1
        res = 0
        odd = 0
        for k, v in hmap.items():
            if v > 0:
                if v%2 == 0:
                    res += v
                else:
                    res += (v-1)
                    odd += 1
            else:
                odd += 1
        return res+1 if odd else res
                
        
        
        
        