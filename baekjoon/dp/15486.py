n = int(input())
T = list()
P = list()
dp = [0]*(n+1)

for _ in range(n):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

# 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램 
for i in range(n):
    time = T[i]
    price = P[i]
    if i+time <= n:
        dp[i+time] =max(dp[i]+price,dp[i+time])
        dp[i+1] = max(dp[i+1],dp[i])
print(dp)