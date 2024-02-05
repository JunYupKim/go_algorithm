n = int(input())
storage = list(map(int,input().split()))
dp = [0]*(n)
if len(storage) > 2: 
    dp[0] = storage[0]
    dp[1] = storage[1]
    for i in range(3,n):
        dp[i] = max(dp[i-1],dp[i-2]+storage[i])

    print(dp[n-1])
else:
    print(max(storage))