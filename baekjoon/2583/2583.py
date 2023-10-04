from collections import deque 

M,N,K = map(int,input().split())
graph = [[0]*(N) for _ in range(M)]
v = [[0]*(N) for _ in range(M)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(y,x):
    cnt = 1
    q = deque()
    q.append((y,x))
    v[y][x] = 1 
    while q: 
        y,x = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= ny<M and 0<=nx<N and graph[ny][nx] == 0 and v[ny][nx] == 0: 
                q.append((ny,nx))
                v[ny][nx] = 1 
                cnt += 1 
    return cnt 

for _ in range (0,K):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1 


answer = 0
area = list() 
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and v[i][j] == 0:
            answer += 1 
            area.append(BFS(i,j)) 

print(answer)
area.sort()
for i in range(len(area)):
    print(area[i], end= ' ')
print()
