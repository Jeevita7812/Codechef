for i in range(int(input())):
    j = int(input())
    s = 0
    while j > 0:
        s += j ** 2
        j -= 2
    print(s)
