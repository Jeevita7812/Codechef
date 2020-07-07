for i in range(int(input())):
    cl, zy = map(int, input().split())
    j = list(map(int,input().split()))
    s = sum(j)
    if s % 2 == 0 and zy == 1:
        print('odd')
    else:
        print('even')
