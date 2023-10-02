N = int(input())
numbers = list(map(int,input().split()))

def check_prime(num):
    if num == 1: 
        return False 
    else:
        cnt = 0 
        for i in range(2,int(num/2)+1):
            if (num%i) == 0: 
                return False
        return True

count_prime = 0 
for n in numbers:
    if check_prime(n) == True:
        count_prime += 1 
    
print(count_prime)

