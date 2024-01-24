N = input()

cnt = 0 
for i in N[len(N)//2:]:
    cnt += int(i)
for i in N[:len(N)//2]:
    cnt -= int(i)
if cnt == 0: 
    print("LUCKY")
else:
    print("READY")
