for i in range(int(input())):
    cl, zy = map(int, input().split())
    s = list(map(int,input().split()))
    j = [0] * cl
    for k in s:
        if(j[k - 1] == min(j)):
            j[k - 1] += 1
        else:
            print("NO")
            break
    else:
        print("YES")
