import re
N = int(input())
word = list()
for _ in range(N):
    S = input()
    word.append(S)
    
answer = list()

for w in word: 
    temp = re.split(r'(\d+)',w)
    for a in temp:
        if a.isdigit():
            answer.append(int(a))

answer.sort()

for _ in range(len(answer)):
    print(answer[_])
 