class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_hmap, t_hmap = defaultdict(str), defaultdict(str)
        for i in range(len(s)):
            if s[i] not in s_hmap:
                s_hmap[s[i]] = t[i]
            if t[i] not in t_hmap:
                t_hmap[t[i]] = s[i]
            if s_hmap[s[i]] != t[i] or t_hmap[t[i]] != s[i]:
                    return False
        return True
        
        