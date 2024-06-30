def solution(n, words):
    answer = [0,0]
    word_table = []
    
    for idx,value in enumerate(words):
        if value not in word_table:
            word_table.append(value)
            if idx > 0 and word_table[idx-1][-1] != value[0]:
                answer = [(idx%n)+1, (idx//n)+1]
                return answer
        else:
            answer = [(idx%n)+1, (idx//n)+1]
            return answer 
    
    return answer