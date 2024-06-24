def solution(participant, completion):
    answer = ''
    temp = dict()
    for i in participant: 
        if i not in temp:
            temp[i] = 1 
        elif i in temp: 
            temp[i] += 1 
    
    for i in completion: 
        if i in temp:
            temp[i] -= 1 
        
    
    for i in temp:
        if temp[i] > 0: 
            answer = i
        
    return answer