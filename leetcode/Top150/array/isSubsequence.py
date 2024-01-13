class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True 

        check = [0]*len(s)
        i = 0 
        for idx in range(len(t)):
            if t[idx] == s[i]:
                check[i] = 1 
                i += 1 
            if check.count(0) == 0:
                return True 

        if check.count(0) >= 1:
            return False
        else:
            return True 