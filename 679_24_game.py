import math

class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # print nums
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-4
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                combinations = [nums[i] + nums[j], nums[i] * nums[j], nums[i]-nums[j], nums[j]-nums[i]]
                if nums[j] != 0:
                    combinations.append(float(nums[i])/float(nums[j]))
                if nums[i] != 0:
                    combinations.append(float(nums[j])/float(nums[i]))
                # print combinations
                cur_nums = [l for k,l in enumerate(nums) if k != i and k != j]
                # print cur_nums
                for comb in combinations:
                    if self.judgePoint24(cur_nums + [comb]) == True:
                        return True
                    
        return False
                
                
