x = int(input())
l = []
for i in range(x):
    sum = 0
    for j in range(10):
        a = str(input()).split(" ")
        for k in a:
            k = int(k)
            if(k <= 30):
                sum += 1
    if(sum >= 60):
        l.append("yes")
    else:
        l.append("no")
