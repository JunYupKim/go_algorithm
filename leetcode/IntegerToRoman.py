class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = {
            1:    'I',
            4:    'IV',
            5:    'V',
            9:    'IX',
            10:    'X',
            40:    'XL',
            50:    'L',
            90:    'XC',
            100:    'C',
            400:    'CD',
            500:    'D',
            900:    'CM',
            1000:    'M'
        }

        answer = ''

        n = str(num)
        A = ''
        temp = ''
        for i in range(len(n)-1,-1,-1):

            temp = int(n[i]+A)
            number = int(n[i])

            if int(n[i]) ==4 or int(n[i]) == 5 or int(n[i])==9:
                answer = roman[temp]+answer
            else:
                if number < 4:
                    answer = roman[int(str(1)+A)]*number+answer
                if number > 5 :
                    answer = roman[int(str(5)+A)]+roman[int(str(1)+A)]*(number-5)+answer
            A += '0'

        return answer 