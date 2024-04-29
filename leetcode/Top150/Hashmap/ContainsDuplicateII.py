class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            target = nums[i]
            dup = nums[i+1:i+k+1]
            if target in dup:
                return True 
        return False 