class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
      
        word = strs[0]
        for idx in range(1,len(strs)):
            if word == strs[idx][:len(word)]:
                continue
            else:
                for i in range(len(word)):
                    if word[:i] == strs[idx][:i]:
                        temp = strs[idx][:i]
                word = temp
        return word