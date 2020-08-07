for i in range(int(input())):
    j, s, c = map(int, input().split())
    if j == s:
        print(0)
    elif c % 2 == 0:
        if abs(j) > abs(s):
            print(1)
        elif abs(j) < abs(s):
            print(2)
        else:
            print(0)
    else:
        if j > s:
            print(1)
        else:
            print(2)
