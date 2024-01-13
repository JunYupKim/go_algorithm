class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0 
        for idx,jump in enumerate(nums):
            # check if idx is over the reach 
            if idx > reach:
                return False
            # update reach 
            reach = max(reach,idx+jump)
            # check if reach is on the target
            if reach >= len(nums)-1:
                return True
        return False 