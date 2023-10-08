from itertools import permutations as p 
S = input()
check = False 
for A in p(S,len(S)):
    if A[::-1]== A[:]:
        print(''.join(A))
        check = True 
        break
if check == False:
    print("I'm Sorry Hansoo")