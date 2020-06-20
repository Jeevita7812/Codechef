for i in range(int(input())):
    j = input()
    s = []
    s.append(j[0])
    s.append(j[1])
    c = 1
    for k in range(len(j)-1):
        if j[k] != j[k + 1]:
            if j[k] and j[k + 1] in s:
                c +=1
            else:
                print("NO")
                break
        else:
            print("NO")
            break
    if len(j) == c:
        print("YES")
