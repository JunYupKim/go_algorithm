N = int(input())
S = input()
num = list()
op = list()
answer = -999999999

def oper(number1, operation,number2):
    if operation == '*':
        return number1*number2
    
    if operation =='-':
        return number1-number2

    if operation =='+':
        return number1+number2

# 일단 나누고 
for i in range(N):
    if S[i].isdigit():
        num.append(int(S[i])) 
    else:
        op.append(S[i])

def go(idx,sum):
    global answer
    if idx == N-1: 
        answer = max(answer,sum)
        return 
    # left to right 
    go(idx+1,oper(sum,op[idx],num[idx+1]))
    # if left to right +2 
    if idx+2 <= N-1: 
        tmp = oper(num[idx+1],op[idx+1],num[idx+2])
        go(idx+2,oper(sum,op[idx],tmp)) 
    return 

go(0,num[0])

print(answer)
