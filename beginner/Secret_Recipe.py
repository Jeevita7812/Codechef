for i in range(int(input())) :
    j, s, cy, yl, b = map(int,input().split())
    t = (abs(cy - j))/yl
    p = ( abs(cy - s) ) / b
    if t < p :
        print("Chef")
    elif t > p :
        print("Kefa")
    else :
        print("Draw")
