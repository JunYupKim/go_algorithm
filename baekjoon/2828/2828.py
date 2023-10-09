# N : 스크린 N칸
# M : M 칸을 차지하는 바구니 
N,M = map(int,input().split())
J = int(input())

# 바구니가 이동해야 하는 거리의 최솟값 
answer = 0 
# 1부터 시작 
left = 0
right = left+M-1

for _ in range(J):
    pos = int(input())-1
    if right < pos:
        answer += (pos-right)
        left += (pos-right)
        right += (pos-right) 
    elif pos < left:  
        answer += (left-pos)
        right -= (left-pos)
        left -= (left-pos)

print(answer)


