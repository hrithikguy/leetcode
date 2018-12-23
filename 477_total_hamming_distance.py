class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        maximum = max(nums)
        output = 0
        while maximum > 0:
            cur_max = 0
            num_ones = 0
            for i,j in enumerate(nums):
                if j % 2 == 1:
                    num_ones += 1
                nums[i] /= 2
                cur_max = max(cur_max, nums[i])
            output += num_ones * (len(nums) - num_ones)
            maximum = cur_max
            
        return output
