N,C = map(int,input().split())
arr = list(map(int,input().split()))
answer = dict()
idx = 1 
for e in arr: 
    if e not in answer: 
        answer[e] = [1,idx] 
    else:
        answer[e][0] += 1 
        idx+=1 

answer = [[i,j] for i,j in answer.items()]

answer.sort(key=lambda x:(-x[1][0],x[1][1]))

result = list()

for a in answer:
    result += [a[0]]*a[1][0]

for i in result:
    print(i,end=' ')


