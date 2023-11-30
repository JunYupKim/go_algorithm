N = int(input())
S = input()

ret = -1e9

def oper(num1, op,num2):
    if op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1*num2
    return 

number = list()
operation = list()

for i in range(N):
    if S[i].isdigit():
        number.append(int(S[i]) )
    else:
        operation.append(S[i])

def go(idx, num):
    if idx == len(S)-1:
        ret = max(num,ret)
        return 
    go(idx+1,oper(num,operation[idx], number[idx+1]))
    if(idx+2 <= N-1):
        temp = oper(number[idx+1],operation[idx+1],number[idx+2])
        go(idx+2,oper(num,operation[idx], temp))
    return 

go(0,number[0])
print(ret)