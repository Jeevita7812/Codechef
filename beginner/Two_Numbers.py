for i in range(int(input())):
    j, s, n = map(int, input().split())
    if n % 2 == 0:
        print(max(s,j)//min(s,j))
    else:
        j = j * 2
        print(max(j,s)//min(j,s))
