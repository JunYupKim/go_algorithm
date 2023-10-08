from collections import deque 
M,N = map(int,input().split())
graph = list()
for _ in range(N):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 토마토가 익을 때까지 최소 날짜 출력 
# 1 : 토마토 
# 0 : 익지 않은 토마토 

def check():
    count_zero = 0 
    for _ in range(N):
        count_zero += graph[_].count(0)
    return count_zero

def BFS(tomato):
    q = deque()
    for y,x in tomato:
        q.append((y,x))

    while q: 
        y,x = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<M and 0<=ny<N:
                if graph[ny][nx] == 0: 
                    graph[ny][nx] = graph[y][x]+1 
                    q.append((ny,nx)) 

tomato_loc = list()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1: 
            tomato_loc.append((i,j))

BFS(tomato_loc)

# 만약 토마토 상자에 0이 존재한다면 
if check()>0 : 
    print(-1)
else:
    day = 0 
    for i in range(N):
        day = max(day,max(graph[i]))
    print(day-1)

