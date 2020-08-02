for i in range(int(input())):
    c = int(input())
    s = list(map(int,input().split()))
    s.sort(reverse=True)
    j = 0
    for k in range(c):
        if s[k] - k >= 0:
            j = j + s[k] - k 
    print(j % ((10 ** 9) + 7)) 
