from itertools import combinations as c
N,M = map(int,input().split())
graph = list()
for _ in range(N):
    graph.append(list(map(int,input().split())))

# 0 : 빈칸
# 1 : 집
# 2 : 치킨집 
house = list()
chicken = list()
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i,j))
        if graph[i][j] == 2: 
            chicken.append((i,j))

answer = 1e9 
for a in c(chicken,M):
    chk = [[0]*(N)  for _ in range(N)] 
    for y1,x1 in a: 
        for y2,x2 in house:
            number = abs(y1-y2)+abs(x1-x2) 
            if chk[y2][x2] != 0:
                chk[y2][x2] = min(number,chk[y2][x2])
            if chk[y2][x2] == 0: 
                chk[y2][x2] = number
    s = 0 
    for _ in range(N):
        s += sum(chk[_])
    answer = min(answer,s)
print(answer)