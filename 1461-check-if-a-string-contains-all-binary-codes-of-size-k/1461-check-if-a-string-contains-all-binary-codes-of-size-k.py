class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hset = set()
        for i in range(len(s)+1-k):
            hset.add(s[i:i+k])
        return True if len(hset) == 2**k else False 