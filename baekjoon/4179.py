from collections import deque 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

R,C = map(int,input().split())
f_v = [[1e9]*C for _ in range(R)]
j_v = [[0]*C for _ in range(R)]

graph = list()
for _ in range(R):
    graph.append(list(input().rstrip()))

# 지훈 
jihoon_loc = list()
# Fire 
fire_loc = list()
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':
            jihoon_loc.append((i,j))
        if graph[i][j] == 'F':
            fire_loc.append((i,j))


def j_BFS(y,x):
    j_v[y][x] = 1
    q = deque()
    q.append((y,x))
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+ dy[i]
            nx = x+dx[i]
            if 0<=ny<R and 0<=nx<C:
                if  f_v[ny][nx] <= j_v[y][x]+1:
                    continue 
                if graph[ny][nx] == '.' and j_v[ny][nx] == 0:
                    j_v[ny][nx] = j_v[y][x] + 1 
                    q.append((ny,nx))
            else:
                return j_v[y][x]
    return -1  

def f_BFS():
    q = deque()
    for y,x in fire_loc:
        f_v[y][x] = 1 
        q.append((y,x))
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+ dy[i]
            nx = x+dx[i]
            if 0<=ny<R and 0<=nx<C:
                if graph[ny][nx] == '.' and f_v[ny][nx] == 0:
                    f_v[ny][nx] = f_v[y][x] + 1 
                    q.append((ny,nx))
            else:
                return f_v[y][x]

y,x = jihoon_loc.pop(0)
f_shortest_path = f_BFS()
j_shortest_path = j_BFS(y,x)


if j_shortest_path == -1:
    print("IMPOSSIBLE")
else:
    print(j_shortest_path)