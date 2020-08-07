for i in range (int(input())):
    l = int(input())
    s = map(int,input().split())
    j = 0
    for c in s:
        if c % 2 == 0:
            print("No")
            j = 1 
            break
    if j == 0:
        print("Yes")
