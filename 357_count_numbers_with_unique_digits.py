class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        for i in range(n+1):
            if i == 0:
                dp[i] = 1
                continue
            elif i == 1:
                dp[i] = 9
                continue
            elif i == 2:
                dp[i] = 81
                continue
            else:
                dp[i] = dp[i-1] * (11 - i)
                
        
        print dp
        output = 0
        for i in range(n+1):
            output += dp[i]
            
        return output
        
        
