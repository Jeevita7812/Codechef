for i in range(int(input())):
    n = int(input())
    delay = 0
    for j in range(n):
        a, b = map(int,input().split())
        if b - a > 5:
            delay += 1
    print(delay)
