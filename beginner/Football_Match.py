for i in range(int(input())):
    s = []
    for b in range(int(input())):
        lt = input()
        s.append(lt)
    c = list(set(s))
    j = 0
    for ky in s:
        if(ky == c[0]):
            j += 1
        else:
            j -= 1
    if(j > 0):
        print(c[0])
    elif(j < 0):
        print(c[1])
    else:
        print("Draw")
