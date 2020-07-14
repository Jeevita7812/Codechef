for i in range(int(input())):
    j = int(input())
    c, l = map(int, input().split())
    y, z = map(int, input().split())
    s, b = map(int,input().split())
    at = (((c - y) ** 2) + ((l - z) ** 2)) ** 0.5
    r = (((c - s) ** 2) +((l - b) ** 2)) ** 0.5
    t = (((y - s) ** 2) + ((z - b) ** 2)) ** 0.5
    if(r <= j and at <= j):
        print("yes")
    elif(r <= j and t <= j):
        print("yes")
    elif(t <= j and at <= j):
        print("yes")
    else:
        print("no")
