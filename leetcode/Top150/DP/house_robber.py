class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
      
        if len(nums) == 1: 
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        dp =[0]*(len(nums)+1)

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2]+dp[0]

        for i in range(3,len(nums)):
            dp[i] = nums[i]+max(dp[i-2],max(dp[:i-2]))

        return max(dp)
  