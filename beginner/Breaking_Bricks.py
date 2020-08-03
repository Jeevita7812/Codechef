for i in range(int(input())):
    j = list(map(int, input().split()))
    s = j[0]
    if(j[1] + j[2] + j[3] <= s):
        print(1)
    elif((j[1] + j[2]) <= s or (j[2] + j[3]) <= s):
        print(2)
    else:
        print(3)
