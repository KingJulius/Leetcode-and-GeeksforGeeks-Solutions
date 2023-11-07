class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = [0]*26
        for i in range(len(s)):
            s_count[ord(s[i])-ord('a')] += 1
        for i in range(len(t)):
            s_count[ord(t[i])-ord('a')] -= 1
        return [0]*26 == s_count