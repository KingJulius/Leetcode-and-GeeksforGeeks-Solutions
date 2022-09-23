class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        def isLetter(c):
            return (ord('a')<=ord(c)<=ord('z')) or (ord('A')<=ord(c)<=ord('Z'))
        s_list = list(s)
        l, r = 0, len(s_list)-1
        while l<r:
            while l<r and not isLetter(s_list[l]):
                l += 1
            while l<r and not isLetter(s_list[r]):
                r -= 1
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1
        return "".join(s_list)