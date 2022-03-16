class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        i, j = 0, 0
        maxLen = 0
        while j < len(s):
            if s[j] not in hmap:
                hmap[s[j]] = 1
            else:
                hmap[s[j]] += 1
                
            if len(hmap) == j-i+1:
                maxLen = max(maxLen, j-i+1)
            else:
                while len(hmap) < j-i+1:
                    hmap[s[i]] -= 1
                    if hmap[s[i]] == 0:
                        hmap.pop(s[i])
                    i += 1
            j += 1
        return maxLen