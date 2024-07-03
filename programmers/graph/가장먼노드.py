from collections import deque,defaultdict
def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)] 

    distance_record = defaultdict(int)
    
    for x,y in edge:
        graph[x].append(y)
        graph[y].append(x)

    def BFS():
        max_dist = 0 
        q = deque()
        q.append((1,0))
        v = [0]*(n+1)
        v[1] = 1
        while q:
            node,dist = q.popleft()
            if max_dist < dist:
                max_dist = dist 
            if max_dist == dist: 
                distance_record[dist] += 1 
            for i in graph[node]:
                if v[i] == 0:
                    v[i] = v[node]+1 
                    q.append((i,dist+1))
        return max_dist
    
    return distance_record[BFS()]
