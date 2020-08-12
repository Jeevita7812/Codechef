for i in  range(int(input())):
    s = list(map(int,input().split()))
    c = s[-1]
    j = 0 
    for kb in s[:-1] :
        j += (c * kb)
    if j > 120 : 
        print("Yes")
    else : 
        print("No")
