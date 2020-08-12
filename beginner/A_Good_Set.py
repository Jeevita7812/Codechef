for i in range(int(input())):
    s = int(input())
    j = []
    if(s == 1):
        print("1")
    elif(s == 2):
        print("1 2")
    else:
        zy = 1
        j.append(1)
        c = 1
        while(zy < s):
            j.append(j[c - 1] + 2)
            zy += 1
            c += 1
        for kb in j:
            print(kb,end = " ")
        print()
