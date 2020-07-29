for i in range(int(input())):
    j, s, c = map(int, input().split())
    if abs(j + s) == c or abs(j + c) == s or abs(s + c) == j:
        print("yes")
    else:
        print("no")
