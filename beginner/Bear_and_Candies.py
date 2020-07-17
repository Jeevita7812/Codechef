for i in range(int(input())):
    cl, zy = map(int, input().split())
    j = 1
    s = 0
    b = 0
    while(True):
        if j % 2 == 0:
            s += j 
            if s > zy:
                print("Limak")
                break
        else:
            b += j
            if b > cl:
                print("Bob")
                break
        j += 1
