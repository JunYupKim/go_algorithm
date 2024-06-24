def solution(want, number, discount):
    answer = 0

    
    for idx in range(len(discount)-9):
        temp_list = discount[idx:idx+10]
        
        temp = dict()
        for i in range(len(want)):
            temp[want[i]] = number[i]
   
        for i in want:
            if i not in temp_list:
                break 
            else:
                temp[i] -= temp_list.count(i) 
        for k,v in enumerate(temp):
            if temp[v] != 0:
                break
        else:
            answer += 1 
    
        
            
    
            
            
            
    
    return answer