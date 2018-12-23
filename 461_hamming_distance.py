class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        output = 0
        while xor > 0:
            output += xor & 1
            xor = xor >> 1
            
        return output
