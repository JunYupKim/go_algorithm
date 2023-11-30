from itertools import permutations as p 
from collections import deque 

N = int(input())
SCV = list(map(int,input().split()))
attack = [9,3,1]
attacks = list()
for a,b,c in p(attack,3):
    attacks.append([a,b,c])

v = [[[0] * (64) for i in range(64)] for j in range(64)]

def BFS():
    v[SCV[0]][SCV[1]][SCV[2]] = 1 
    q = deque()
    q.append((SCV[0],SCV[1],SCV[2]))
    while q: 
        a,b,c = q.popleft()
        for i,y,z in attacks:
            na = max(0,a-i)
            nb = max(0,b-y)
            nc = max(0,c-z)
            if v[na][nb][nc] != 0: 
                continue 
            else: 
                v[na][nb][nc] = v[a][b][c] + 1 
                q.append((na,nb,nc))
    return v[0][0][0] - 1 

print(BFS()) 