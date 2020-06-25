for i in range(int(input())):
    n = int(input())
    lst = input().split()
    cy = 0
    if lst[n-1] != 'milk':
        print("NO")
    else:
        for j in range(n-1):
            if lst[j] == 'cookie' and lst[j+1]!= 'milk':
                cy = 1
        if cy == 1:
            print("NO")
        else:
            print("YES")
