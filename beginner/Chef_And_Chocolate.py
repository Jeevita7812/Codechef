for i in range(int(input())):
    j, s = map(int, input().split())
    if j % 2 == 0 or s % 2==0:
        print("Yes")
    else:
        print("No")
