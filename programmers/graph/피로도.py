def solution(k, dungeons):
    answer = -1
    
    def backtrack(hp,cnt,v):
        max_ = cnt 
        for i in range(len(dungeons)):
            min_hp = dungeons[i][0]
            delete_hp = dungeons[i][1]
        
            if v[i] == 0 and min_hp<=hp: 
                v[i] = 1 
                max_ = max(max_,backtrack(hp-delete_hp,cnt+1,v))
                v[i] = 0 
        return max_
    
    
    v = [0]*len(dungeons)

    return backtrack(k,0,v)