for i in range(int(input())):
    j = int(input())
    while(True):
        j += 1
        s = list(str(j))
        if(s.count('3') >= 3):
            print(j)
            break
