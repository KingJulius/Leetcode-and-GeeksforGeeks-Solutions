class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlNum(c: str):
            return (ord('0')<=ord(c)<=ord('9')) or (ord('a')<=ord(c)<=ord('z')) or (ord('A')<=ord(c)<=ord('Z'))
        i, j = 0, len(s)-1
        while i<j:
            while i<j and not isAlNum(s[i]):
                i += 1
            while i<j and not isAlNum(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True