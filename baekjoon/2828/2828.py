# N : 스크린 N칸
# M : M 칸을 차지하는 바구니 
N,M = map(int,input().split())
J = int(input())

# 바구니가 이동해야 하는 거리의 최솟값 
answer = 0
for _ in range(J):
    pos = int(input())
    # if문 사용해서 바구니 안에 있으면 0 
    if pos :
        continue 
    else:
        # 없으면 move 
        answer += abs(M-pos)

print("answer = ",answer)

# 1-1 = 0 
# 5-1 = 4
# 3- = 2 5 1

