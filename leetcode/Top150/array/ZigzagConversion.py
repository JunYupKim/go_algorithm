class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 1 or numRows == 1 or len(s) <= numRows:
            return s 

        idx = 0 
        step = 1 
        sent = [[] for _ in range(numRows)]

        for x in s: 
            sent[idx].append(x) 
            idx += step
            if idx >= numRows-1:
                step = -1 
            if idx == 0:
                step = 1 

        answer = ''
        for _ in range(numRows):
            answer += ''.join(sent[_])

        return answer


            
            