class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # converting all uppercase letter -> lowercase letter
        # removing all non-alphanumeric character
        temp = ''
        for i in s:
            if i.isalpha() or i.isdigit():
                temp += i.lower()

        return temp[:] == temp[::-1]
      