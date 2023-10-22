while True:
    word = input()
    if word == "end":
        break 
    check = [False]*3
    # 1. a,e,i,o,u 
    vowels = ['a','e','i','o','u']
    for v in vowels:
        if v in word:
            check[0] = True 
            break 
    if check[0] is False:
        print("<"+word+">"+" is not acceptable.")
        continue 
    # 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안된다
    check[1] = True 
    for i in range(len(word)-2) :
        if word[i] in vowels and word[i+1] in vowels and word[i+2] in vowels:
            check[1] = False 
        elif not(word[i] in vowels) and not(word[i+1]in vowels) and not(word[i+2] in vowels):
            check[1] = False 
    if check[1] is False:
        print("<"+word+">"+" is not acceptable.")
        continue
    # 3. 같은 글자가 연속적으로 두 번 오면 안되나, ee, oo 허용 
    check[2] = True 
    for i in range(len(word)-1) :
        if word[i] == word[i+1]:
            if word[i] is 'e' or word[i] is 'o':
                continue 
            else:
                check[2] = False 
    if check[2] is False:
        print("<"+word+">"+" is not acceptable.")
        continue

    print("<"+word+">"+" is acceptable.")    
    