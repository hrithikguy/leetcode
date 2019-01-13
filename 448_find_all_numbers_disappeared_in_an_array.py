class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in nums:
            if nums[abs(i)-1] > 0:
                nums[abs(i)-1] *= -1
            
        output = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(i+1)
                
        return output
