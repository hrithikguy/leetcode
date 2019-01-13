class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if 1 <= len(nums) <= 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        
        dp = []
        dp.append(nums[0])
        dp.append(nums[1])
        dp.append(max(nums[2] + nums[0], nums[1]))
        
        for i in range(3,len(nums)):
            dp.append(max(dp[-2], dp[-3]) + nums[i])
            
        return max(dp)
