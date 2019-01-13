class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        for i in range(1, n+1):
            if i <= 2:
                dp[i] = 1
                continue
            else:
                cur_max = 0
                for j in range(1,i):
                    cur_max = max(cur_max, j * (i-j), j * dp[i-j], dp[j] * dp[i-j])
                    
                dp[i] = cur_max
                
            print dp[i]
            
        return dp[n]
            
            
        
        #breaking it into 2 integers:
        # i/2 * i/2 if even
        # (i-1)/2 * (i+1)/2 if odd
        
        #for more than two, need to find k such that
        # max(dp[k] * dp[n-k], k * dp[n-k], k * (n-k)) is maximal
        
        
