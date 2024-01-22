import sys 
sys.setrecursionlimit(10**9)
M,N = map(int,input().split())
graph = list()
for _ in range(M):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
DP = [[0]*N for _ in range(M)]

def DFS(x,y):
    if x== M-1 and y==N-1:
        return 1
    DP[x][y] = 0 
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<M and 0<=ny<N and graph[nx][ny] < graph[x][y]:
            DP[x][y] = DP[x][y] + DFS(nx,ny)    
    return DP[x][y]

print(DFS(0,0)) 
