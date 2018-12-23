import heapq

class Solution(object):
    def num_less_or_equal(self,m,n,val):
        out = 0
        for i in range(1, m+1):
            out += min(n, val/i)
        
        return out
    
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        lo = 1
        hi = m*n
        
        while lo != hi:
            mid = (lo + hi)/2
            numle = self.num_less_or_equal(m,n,mid)
            if numle >= k:
                hi = mid
            else:
                lo = mid+1
                
        return lo
        
        
