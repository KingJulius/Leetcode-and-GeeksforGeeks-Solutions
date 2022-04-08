from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = deque()
        
        # If less than 2 elements
        if len(s) < 2:
            return False
        for c in s:
            if c == "(" or  c == "{" or c == "[":
                stk.append(c)
            elif c == ")" or  c == "}" or c == "]":
                if len(stk) == 0:
                    return False
                if (stk[-1] == "(" and c == ")") or (stk[-1] == "[" and c == "]") or (stk[-1] == "{" and c == "}"):
                    stk.pop()
                else:
                    return False
        
        if len(stk) == 0:
            return True
        else:
            return False