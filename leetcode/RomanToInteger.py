class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        R = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        answer = list()
        idx = 0 
        while idx < len(s):
            if s[idx] in ["I","X","C"] and idx+1 < len(s) and R[s[idx]] < R[s[idx+1]]:

                if s[idx] == "I":
                    if s[idx+1] == "V":
                        answer.append(4)
                    elif s[idx+1] == "X":
                        answer.append(9)
                elif s[idx] == "X":
                        if s[idx+1] == "L":
                            answer.append(40)
                        elif s[idx+1] =="C":
                            answer.append(90)
                elif s[idx] == "C":
                        if s[idx+1] == "D":
                            answer.append(400)
                        elif s[idx+1] == "M":
                            answer.append(900)
                idx += 2
            else:
                answer.append(R[s[idx]])
                idx += 1 
                
        return sum(answer)
        