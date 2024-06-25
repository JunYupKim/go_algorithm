from collections import deque 
def solution(maps):
    answer = 0
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    maps = [list(idx) for idx in maps]

    Start = []
    End = []
    Lever = []
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                Start.append((i,j))
            if maps[i][j] == 'E':
                End.append((i,j))
            if maps[i][j] == 'L':
                Lever.append((i,j))
            if Start != [] and End !=[] and Lever !=[]:
                break

    def BFS(x,y,target_x,target_y):
        q = deque()
        q.append((x,y,0))
        
        v = list()
        for i in range(len(maps)):
            v.append([0]*len(maps))
            
        v[x][y] = 0 
        
        while q: 
            x,y,c = q.popleft() 
            if x == target_x and y == target_y:
                return c
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny] != 'X'and v[nx][ny] == 0:
                        q.append((nx,ny,c+1))
                        v[nx][ny] = 1 
        return -1
    
    Start_To_Lever = BFS(Start[0][0],Start[0][1],Lever[0][0],Lever[0][1])

    Lever_To_End = BFS(Lever[0][0],Lever[0][1],End[0][0],End[0][1])
   
    if Start_To_Lever == -1 or Lever_To_End == -1:
        return -1 
    
    return (Start_To_Lever+Lever_To_End)