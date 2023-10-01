class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_list = set(nums)
 
        for j in nums_list:
            while nums.count(j) != 1: 
                nums.remove(j)
        return len(nums)
        