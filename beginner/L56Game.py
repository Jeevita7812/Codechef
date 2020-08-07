for i in range(int(input())):
    b = int(input())
    j = list(map(int,input().split()))
    s = 0
    for c in j:
        if c % 2 == 1:
            s += 1
    if(len(j) == 1):
        print(1)
    elif(s % 2 == 1):
        print(2)
    else:
        print(1)
