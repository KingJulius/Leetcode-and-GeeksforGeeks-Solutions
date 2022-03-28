class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(" ")
        res = []
        rev_w_str = ""
        for word in reversed(word_list):
            if word != "":
                res.append(word)
        for word in res:
            rev_w_str += word + " "
        return rev_w_str[:-1]
        