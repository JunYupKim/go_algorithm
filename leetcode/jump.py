class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0 
        for idx,jump in enumerate(nums):
            if idx > reach:
                return False
            reach = max(reach,idx+jump)
            if reach >= len(nums)-1:
                return True
        return False 