class NumArray(object):
    psums = []
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.psums = []
        cur = 0
        self.psums.append(0)
        for i in nums:
            cur += i
            self.psums.append(cur)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # print self.psums
        return self.psums[j+1] - self.psums[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
