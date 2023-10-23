H, W = map(int, input().split())
sky = [input() for _ in range(H)]
graph = [[-1]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if sky[i][j] == 'c':
            graph[i][j] = 0 

for i in range(H):
    for j in range(W):
        if graph[i][j] == 0: 
            idx = 1
            for z in range(j+1,W):
                if graph[i][z] == 0: 
                    break 
                graph[i][z] = idx 
                idx += 1 

for i in graph:
    print(*i, end=' ')
    print()