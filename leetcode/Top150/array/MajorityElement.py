class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = set(nums)
        cnt = 0 
        number = 0 
        for i in elements: 
            current = nums.count(i)
            if cnt < current:
                cnt = current 
                number = i 
        return number 
                
            