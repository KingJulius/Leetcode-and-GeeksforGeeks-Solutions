class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        rev_w_str = ""
        for word in reversed(word_list):
            rev_w_str += word + " "
        return rev_w_str[:-1]
        