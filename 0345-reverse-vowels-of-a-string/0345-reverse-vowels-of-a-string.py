class Solution:
    def reverseVowels(self, s: str) -> str:
        # R to L and store vowels in an array
        # T.C: O(n)
        # S.C: O(n)
        vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(s)-1
        s = list(s)
        while i < j:
            if s[i] in vowel_list and s[j] in vowel_list:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            if s[i] not in vowel_list:
                i += 1
            if s[j] not in vowel_list:
                j -= 1
        return "".join(s)
            