from collections import deque 
def solution(maps):
    
    end = [len(maps)-1,len(maps)-1]
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def BFS():
        q = deque()
        q.append((0,0))
        v = [[0]*len(maps[0]) for _ in range(len(maps))] 
        v[0][0] = 1 
        while q:
            x,y = q.popleft()
            for i in range(4): 
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<n and 0<=ny<m and v[nx][ny] == 0:
                    if nx == n-1 and ny == m-1: 
                        return v[x][y]+1
                    if maps[nx][ny] == 1:
                        q.append((nx,ny))
                        v[nx][ny] = v[x][y] + 1 
        return -1 
    
    return BFS()
