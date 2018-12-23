class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_set = {}
        
        for i,j in enumerate(nums):
            if target-j in target_set:
                return [target_set[target-j][0], i]
            else:
                target_set[j] = [i]
