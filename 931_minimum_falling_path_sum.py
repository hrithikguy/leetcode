class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(len(A))[::-1]:
            # print A
            if i == len(A) - 1:
                continue
            for j in range(len(A)):
                # print i,j
                cur_min = 101
                for k in range(j-1, j+2):
                    
                    if 0 <= k < len(A):
                        # print A[i+1][k]
                        cur_min = min(cur_min, A[i+1][k])

                A[i][j] += cur_min
                    
        return min(A[0])
            
