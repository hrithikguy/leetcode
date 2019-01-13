class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        output = 0
        Jset = set(J)
        
        for i in S:
            if i in Jset:
                output += 1
                
        return output
        
