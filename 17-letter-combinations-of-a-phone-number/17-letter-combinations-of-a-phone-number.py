class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        
        list_digits = [2,3,4,5,6,7,8,9]
        list_alphabets=[chr(i) for i in range(97, 123)]
        

        d = {}
        count = 0
        for ele in list_digits:
            str1 = list()
            if ele == 9 or ele == 7:
                i = 0
                while i <4 and count<len(list_alphabets):
                    str1.append(list_alphabets[count])
                    count += 1
                    i += 1
                d[ele] = str1
            else:
                i = 0
                while i<3 and count<len(list_alphabets):
                    str1.append(list_alphabets[count])
                    count += 1
                    i += 1
                d[ele] = str1
        
        if len(digits) == 1:
            return d.get(int(digits[0]))
        
        output = []
        if len(digits) == 2:
            ls0 = d.get(int(digits[0]))
            ls1 = d.get(int(digits[1]))
            for i in range(len(ls0)):
                for j in range(len(ls1)):
                    str1 = str(ls0[i]) + str(ls1[j])
                    output.append(str1)
                    
        elif len(digits) == 3:
            ls0 = d.get(int(digits[0]))
            ls1 = d.get(int(digits[1]))
            ls2 = d.get(int(digits[2]))
            for i in range(len(ls0)):
                for j in range(len(ls1)):
                    for k in range(len(ls2)):
                        str1 = str(ls0[i]) + str(ls1[j]) + str(ls2[k])
                        output.append(str1)
        
        elif len(digits) == 4:
            ls0 = d.get(int(digits[0]))
            ls1 = d.get(int(digits[1]))
            ls2 = d.get(int(digits[2]))
            ls3 = d.get(int(digits[3]))
            for i in range(len(ls0)):
                for j in range(len(ls1)):
                    for k in range(len(ls2)):
                        for l in range(len(ls3)):
                            str1 = str(ls0[i]) + str(ls1[j]) + str(ls2[k]) + str(ls3[l])
                            output.append(str1)
        return output
            
        

                
            
                