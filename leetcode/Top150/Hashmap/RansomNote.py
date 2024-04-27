class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = dict()
        for i in range(len(magazine)):
            char = magazine[i]
            if char in d:
                d[char] += 1 
            else:
                d[char] = 1 
        
        for i in range(len(ransomNote)):
            char = ransomNote[i]
            if char not in d:
                return False
            else:
                if d[char] > 0: 
                    d[char] -= 1 
                else:
                    return False 
        return True 

        
        