class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmap = defaultdict(int)
        for c in magazine:
            hmap[c] += 1
        for c in ransomNote:
            hmap[c] -= 1
            if hmap[c] < 0:
                return False
        return True