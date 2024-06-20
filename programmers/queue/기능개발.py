from collections import deque 
def solution(progresses, speeds):
    answer = []
    q = deque()
    
    # progresses 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 
    # speeds 각 작업의 개발 속도 
    # 각 배포마다 몇 개의 기능이 배포되는지를 return 
    
    # count days 
    for p in progresses: 
        q.append(p)
    
    while q: 
        # update progress 
        for idx in range(len(q)): 
            q[idx] += speeds[idx]
            
        cnt = 0 
        
        if q[0] >= 100:
            for i in range(len(q)):
                if q[0] >= 100:
                    q.popleft()
                    speeds.pop(0)
                    cnt += 1 
                else:
                    break 
            
            answer.append(cnt)
        
    return answer