class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==1:
            return True
        
        s_new = ""
        
        for char in s:
            if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
                s_new += char.lower()
            elif (ord(char) >= 48 and ord(char) <= 57):
                s_new += char
        
        #print(s_new)
        if len(s_new)==1:
            return True
        
        i = 0
        j = len(s_new) - 1
        
        while i<=j:
            if s_new[i] != s_new[j]:
                return False
            i += 1
            j -= 1
        
        return True
        
        