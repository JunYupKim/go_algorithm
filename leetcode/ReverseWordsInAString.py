class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = list()

        for i in s.split():
            word_list.append(i) 

        word_list.reverse()

        answer = ''

        for i in range(len(word_list)-1):
            answer += word_list[i] + ' '
        answer += word_list[-1]
        return answer