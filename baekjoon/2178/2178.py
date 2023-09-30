from collections import deque 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):

    q = deque()
    q.append((x,y))

    while q: 
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx<N and 0<=ny<M:
                if graph[nx][ny] == 1: 
                    graph[nx][ny] = graph[x][y]+1 
                    q.append((nx,ny))  
                        
    return graph[N-1][M-1]

N,M = map(int,input().split())
graph = list()

for i in range(N):
    graph.append(list(map(int,input())))


print(BFS(0,0))
