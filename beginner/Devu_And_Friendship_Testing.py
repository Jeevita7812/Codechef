for i in range(int(input())):
    c = int(input())
    s = list(map(int,input().split()))
    j = []
    for k in s:
        if(k not in j):
            j.append(k)
    if(len(j)==len(s)):
        print(len(s))
    else:
        print(len(j))
