from itertools import combinations as c 

def solution(orders, course):
    
    answer = []
    for number_of_course in course:
        food = dict()
        for order in orders:
            for a in c(sorted(order),number_of_course):
                word = str(''.join(a)) 
                if word not in food: 
                    food[word] = 0
                food[word] += 1
                
        food = sorted(food.items(), key=lambda x:x[1],reverse=True)
        
        max_v = 0 
        for k,v in food:
            if max_v < v: 
                max_v = v 
        for k,v in food: 
            if max_v > v: 
                break 
            if v != 1: 
                answer.append(k)
        
    answer.sort()
    
    return answer