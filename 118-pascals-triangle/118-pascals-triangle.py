class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal_list = []
        if numRows == 0:
            return pascal_list
        
        if numRows >= 1:
            pascal_list.append([1])
        
        if numRows >= 2:
            pascal_list.append([1,1])
        

        
        #print(pascal_list[0][0])
        for i in range(3, numRows+1):
            temp_list = []
            temp_list.append(1)
            for j in range(0, i-2):
                temp_list.append(pascal_list[i-2][j] + pascal_list[i-2][j+1])
            temp_list.append(1)
            pascal_list.append(temp_list)
    
        return pascal_list