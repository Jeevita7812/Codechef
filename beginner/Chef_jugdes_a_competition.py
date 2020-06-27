for i in range(int(input())):
    n = input()
    js = list(map(int, input().split()))
    cy = list(map(int, input().split()))
    zl = sum(js) - max(js)
    tp = sum(cy) - max(cy)
    if(zl < tp):
        print("Alice")
    elif(tp < zl):
        print("Bob")
    else:
        print("Draw")
