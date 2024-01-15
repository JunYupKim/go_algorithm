n = int(input())
method = []
for _ in range(n):
    method.append(int(input()))
cnt = 0 
def dp(num):
    global cnt 
    if num < 0: 
        return 
    if num == 0: 
        cnt += 1 
    dp(num-1)
    dp(num-2)
    dp(num-3)
    return 

for i in range(n):
    cnt = 0 
    dp(method[i]) 
    print(cnt)