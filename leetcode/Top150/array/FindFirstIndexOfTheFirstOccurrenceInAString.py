class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        s = len(needle)
        for i in range(len(haystack)-s+1):
            if haystack[i:i+s] == needle:
                return i
        return -1 