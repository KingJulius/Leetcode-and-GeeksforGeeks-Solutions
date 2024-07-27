class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 2 Pointer Approach
        # T.C: O(m+n)
        # S.C = O(1)
        # i, j = 0, 0
        # w1_len = len(word1)
        # w2_len = len(word2)
        # res = []
        # while i < w1_len or j < w2_len:
        #     if i < w1_len:
        #         res.append(word1[i])
        #         i += 1
        #     if j < w2_len:
        #         res.append(word2[j])
        #         j += 1
        # return "".join(res)
        
        # 1 Pointer Approach
        res= []
        max_len = max(len(word1), len(word2))
        for i in range(max_len):
            if i < len(word1):
                res.append(word1[i])
            if i < len(word2):
                res.append(word2[i])
        return "".join(res)
        
        
        
        