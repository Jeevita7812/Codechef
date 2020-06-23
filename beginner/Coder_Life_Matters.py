for i in range(int(input())):
    s = list(map(int,input().split()))
    c = 0
    j = 0
    for y in s:
        if(y == 0):
            c = 0
        if(y == 1):
            c += 1
            if(c > 5):
                j = 1
    if(j == 0):
        print('#allcodersarefun')
    else:
        print('#coderlifematters')
