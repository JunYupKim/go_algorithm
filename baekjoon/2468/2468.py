from collections import deque 

N = int(input())
graph = list()
for _ in range(N):
    graph.append(list(map(int,input().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0 
for h  in range(1,101):
    v = [[0]*N for _ in range(N)] 
    def BFS(y,x):
        v[y][x] = 1 
        q = deque()
        q.append((y,x))
        while q: 
            y,x = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N and graph[ny][nx] < h and v[ny][nx] ==0:
                    v[ny][nx] = 1 
                    q.append((ny,nx))


    def BFS_safe(y,x):
        v[y][x] = 1 
        q = deque()
        q.append((y,x))
        while q: 
                y,x = q.popleft()
                for i in range(4):
                    nx = x+dx[i]
                    ny = y + dy[i]
                    if 0<=nx<N and 0<=ny<N and v[ny][nx] ==0:
                        v[ny][nx] = 1 
                        q.append((ny,nx))

        

    # 높이는 N 
    # 잠기는 지역 파악 
    for i in range(N):
        for j in range(N):
            if graph[i][j] < h and v[i][j] == 0:
                BFS(i,j)
    temp_answer = 0 
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0: 
                temp_answer += 1
                BFS_safe(i,j)
    answer = max(answer,temp_answer)

print(answer)