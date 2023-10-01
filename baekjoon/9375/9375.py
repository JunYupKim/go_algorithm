N = int(input())

for _ in range(N):
    clothe = dict()
    n = int(input())
    for _ in range(n):
        c, kind = map(str, input().split())
        if kind not in clothe:
            clothe[kind] = 1
        else:
            clothe[kind] += 1 

    # count 
    cnt = 1 
    for i in clothe:
        cnt *= (clothe[i]+1)
    cnt -= 1 
    print(cnt)
        