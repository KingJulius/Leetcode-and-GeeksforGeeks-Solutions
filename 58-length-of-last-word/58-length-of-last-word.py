class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        count = 0
        while i >= 0:
            if s[i] != " ":
                count += 1
                i -= 1
            elif count > 0 and s[i] == " ":
                break
            else:
                i -= 1
        return count