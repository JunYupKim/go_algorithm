# https://www.acmicpc.net/problem/13913
# 숨박꼭질 4
from collections import deque 
# N : 수빈이의 위치 
# K : 동생의 위치 
N,K = map(int,input().split())
time = 0 
max_n = 200001
visited = [0]*max_n
dist = [0]*max_n
dx = [2,1,-1]

# 완전 탐색 사용 (BFS)
def BFS(here):
    q = deque()
    q.append(here)
    while q:
        here = q.popleft()
        if here == K:
            return visited[K] 
        for next_ in (2*here,here+1,here-1):
            if max_n >= next_>= 0 and visited[next_] == 0: 
                visited[next_] = visited[here] + 1
                dist[next_] = here 
                q.append(next_)        
# output
# 1. 가장 빠른 시간 
print(BFS(N)) 
# 2. 어떻게 이동해야 하는 지 
i = K 
answer = list()
while i != N: 
    answer.append(i)
    i = dist[i]
answer.append(N)
answer.reverse()
for i in range(len(answer)):
    print(answer[i], end= ' ')
print()

    