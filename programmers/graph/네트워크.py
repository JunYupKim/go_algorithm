def solution(n, computers):
    
    answer = 0
    
    v = [0]*len(computers)

    def DFS(idx):
        v[idx] = 1 
        if idx >= len(computers):
            return 
        for j in range(len(computers[idx])):
            if idx != j and computers[idx][j] == 1 and v[j] == 0: 
                DFS(j)
        return 
    
    network_count = 0 

    for i in range(len(computers)):
        if v[i] == 0 and computers[i][i] == 1:    
            network_count += 1 
            DFS(i)

    return network_count 