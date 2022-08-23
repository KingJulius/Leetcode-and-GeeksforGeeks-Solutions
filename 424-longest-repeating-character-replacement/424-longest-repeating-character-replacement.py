class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = defaultdict(int)
        res = 0
        i, j = 0, 0
        while j < len(s):
            hmap[s[j]] += 1
            while (j-i+1) - max(hmap.values()) > k:
                hmap[s[i]] -= 1
                i += 1
            res = max(res, j-i+1)
            j += 1
        return res
            
            