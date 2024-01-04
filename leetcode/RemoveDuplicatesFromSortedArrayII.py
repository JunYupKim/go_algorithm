class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        more_number = list()
        for i in nums:
            if nums.count(i) > 2:
                if i not in more_number: 
                    more_number.append(i)
                
        for i in more_number:
            for j in range(nums.count(i)-2):
                nums.remove(i) 

        print(nums)
            
        
             
        