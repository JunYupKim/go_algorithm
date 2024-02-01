class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False 

        left_ = ['(','[','{']

        temp = list()
        cnt = len(s)
        for el in s: 
            if el in left_:
                if el == '(':
                    temp.append(')')
                elif el == '[':
                    temp.append(']')
                elif el == '{':
                    temp.append('}')
                cnt -= 1 

            if len(temp) >= 1 and el == temp[-1]:
                temp.pop()
                cnt -= 1 

        if len(temp) == 0 and cnt ==0 :
            return True
        else:
            return False 