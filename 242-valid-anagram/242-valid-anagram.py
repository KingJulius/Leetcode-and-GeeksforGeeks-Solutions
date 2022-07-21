class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_counter = [0] * 26
        t_counter = [0] * 26
        for i in range(len(s)):
            s_counter[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            t_counter[ord(t[i]) - ord('a')] += 1
        hmap = defaultdict(int)
        hmap[tuple(s_counter)] += 1
        hmap[tuple(t_counter)] += 1
        return True if hmap[tuple(s_counter)] == 2 else False