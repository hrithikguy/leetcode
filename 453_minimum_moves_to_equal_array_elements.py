class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = min(nums)
        out = 0
        for i in nums:
            out += i - minimum
        return out
