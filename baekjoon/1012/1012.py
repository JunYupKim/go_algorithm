from collections import deque 

dx = [-1,1,0,0]
dy = [0,0,-1,1]
T = int(input())
for _ in range(T):
    
    def BFS(y,x):
        q = deque()
        q.append((y,x))
        graph[y][x] = 0 
        while q: 
            y,x = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=ny<N and 0<=nx<M and graph[ny][nx] == 1: 
                    graph[ny][nx] = 0 
                    q.append((ny,nx))

    cnt = 0 
    M,N,K = map(int,input().split())
    graph = [[0]*M for _ in range(N)] 
    for _ in range(K):
        X,Y = map(int,input().split())
        graph[Y][X] = 1 
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                cnt += 1 
                BFS(i,j)
    print(cnt)
    
            



