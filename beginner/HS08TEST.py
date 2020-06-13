x,y = input().split()
x = int(x)
y = float(y)
if x % 5 == 0:
    if y >= x + 0.5:
        z = y-x
        print("%0.2f"%float(z-0.5))
    else:
        print("%0.2f"%float(y))
else:
    print("%0.2f"%float(y))
