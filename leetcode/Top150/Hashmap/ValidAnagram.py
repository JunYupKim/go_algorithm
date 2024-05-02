class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        word = dict()
        for i in range(len(s)):
            if s[i] in word:
                word[s[i]] += 1
            else:
                word[s[i]] = 1 
        
        for char in t: 
            if char in word:
                if word[char] > 0:
                    word[char] -= 1 
                else:
                    return False
            else:
                return False 
        for idx,value in enumerate(word):
            if word[value] >= 1: 
                return False 
        return True 
        