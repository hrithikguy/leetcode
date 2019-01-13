class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = []
        dp.append(nums[0])
        
        for i in range(1, len(nums)):
            dp.append(max(dp[-1]+nums[i], nums[i]))
        
                
        
            
        
        
        return max(dp)
