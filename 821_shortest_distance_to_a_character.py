class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        C_idx = [-100000, -100000]
        for i,j in enumerate(S):
            if j == C:
                C_idx.append(i)
        C_idx.append(100000)
        C_idx.append(10000000)
        
        print C_idx
        
        cur_next = 2
        output = []
        for i in range(len(S)):
            output.append(min(abs(i-C_idx[cur_next]), abs(i-C_idx[cur_next-1]), abs(i-C_idx[cur_next+1])))
            if i == C_idx[cur_next]:
                cur_next += 1
                
        return output
        
