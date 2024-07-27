class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 2 Pointer Approach
        # T.C: O(m+n)
        # S.C = O(1)
        i, j = 0, 0
        w1_len = len(word1)
        w2_len = len(word2)
        res = []
        while i < w1_len or j < w2_len:
            if i < w1_len:
                res.append(word1[i])
                i += 1
            if j < w2_len:
                res.append(word2[j])
                j += 1
        return "".join(res)

        
        
        
        