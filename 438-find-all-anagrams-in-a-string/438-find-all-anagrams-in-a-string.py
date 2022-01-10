class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        output = list()
        d = dict()
        for i in range(len(p)):
            if p[i] in d:
                d[p[i]] += 1
            else:
                d[p[i]] = 1
        count = len(set(p))
        
        
        i, j = 0, 0
        while j < len(s):
            if s[j] in d.keys():
                d[s[j]] -= 1
            if s[j] in d.keys():
                if d[s[j]] == 0:
                    count -= 1
            if j -i + 1 < len(p):
                j += 1
            elif j - i + 1 == len(p):
                if count == 0:
                    output.append(i)
                if s[i] in d.keys():
                    d[s[i]] += 1
                if s[i] in d.keys():
                    if d[s[i]] == 1:
                        count += 1
                i += 1
                j += 1

        return output