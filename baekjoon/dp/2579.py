n = int(input())

stair = list()

for _ in range(n):
    stair.append(int(input()))

# 1. 계단은 한 번에 한 계단씩 또는 두 계단 씩 오를 수 있다. 
# 2. 연속된 세 개의 계단은 밟을 수 없다 
# 3. 마지막 도착 계단은 반드시 밟아야 한다

dp = [0]*(n)

dp[0] = stair[0]
for i in range(1,n):
    if i == 1: 
        dp[i] = stair[0]+stair[1]
    elif i == 2:
        dp[i] = stair[2]+max(stair[1],stair[0])
    else:
        dp[i] = max(stair[i-1]+stair[i]+dp[i-3],stair[i]+dp[i-2])
print(dp[-1])