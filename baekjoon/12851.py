# N: 수빈이의 위치 
# K: 동생의 위치 

# x-1 or x+1
# 2*x 

# 가장 빠른 시간으로 찾는 방법이 몇 가지인지 구하는 프로그램 

# output : 가장 빠른 시간을 출력한다. 
# output : 가장 빠른 시간으로 수빈이가 도생을 찾는 방법의 수를 출력한다. 
from collections import deque
N,K = map(int,input().split())
v = [0]*100
answer = 0 

def BFS(x):
    global answer
    q = deque()
    q.append(x) 
    while q: 
        x = q.popleft()
        for nx in [x+1,x-1,x*2]:
            if 0<=nx and nx <= 1e9:
                if v[nx] == 0: 
                    q.append(nx)
                    v[nx] += v[x]+1 
BFS(N)

print(v)