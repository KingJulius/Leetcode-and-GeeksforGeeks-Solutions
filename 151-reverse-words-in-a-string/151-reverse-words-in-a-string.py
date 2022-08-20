class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        rev_w_str = " ".join(word_list[::-1])
        return rev_w_str
        