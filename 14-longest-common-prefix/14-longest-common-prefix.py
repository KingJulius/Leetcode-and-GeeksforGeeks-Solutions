class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str_output = ""
        
        if len(strs)==0:
            return str_output
        
        first_word = strs[0]
        flag = 0
        count = 0
        
        
        for i in range(len(first_word)):
            for j in range(1, len(strs)):
                word = strs[j]
                if len(word) > i:
                    if first_word[i] != word[i]:
                        flag = 1
                else:
                    flag = 1
            if flag != 1:
                count += 1
            else:
                break
        #print(count)
        return first_word[:count]
            
            
        