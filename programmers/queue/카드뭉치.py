from collections import deque 

def solution(cards1, cards2, goal):
    answer = ''
    
    c1 = deque()
    c2 = deque()
    
    for i in cards1:
        c1.append(i)
    for i in cards2:
        c2.append(i)
        
    q = list()
    idx = 0 
    
    while c1 or c2: 
        if c1 and c1[0] == goal[idx]:
            q.append(c1.popleft())
            idx += 1
            
        elif c2 and c2[0] == goal[idx]:
            q.append(c2.popleft())
            idx += 1 

        else:
            break
        
            
    if q == goal:
        return "Yes"
    else:
        return "No"
    
