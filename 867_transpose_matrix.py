class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        output = []
        
        for i in range(len(A[0])):
            cur = [row[i] for row in A]
            output.append(cur)
            
        # output = [row[i] for row in A for i in range(len(A[0]))]
            
        return output
        
