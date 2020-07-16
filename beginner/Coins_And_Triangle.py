for i in range(int(input())):
    cl = int(input()) 
    js = 1
    zy = 0
    while(zy + js <= cl):
        zy += js
        js += 1
    if zy == cl:
        print(js - 1)
    else:
        print(js - 1)
