class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros_start = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zeros_start] = nums[i] 
                zeros_start += 1
                
        for i in range(zeros_start, len(nums)):
            nums[i] = 0
            
            
