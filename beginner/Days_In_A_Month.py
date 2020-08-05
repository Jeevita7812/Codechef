for i in range(int(input())):
    j, m = input().split()
    j = int(j)
    if(j >= 28 and j <= 31):
        s = [4,4,4,4,4,4,4]
        c = {"mon":0,"tues":1,"wed":2,"thurs":3,"fri":4,"sat":5,"sun":6}
        z = j - 28
        y = 0
        for k in c:
            if k == m:
                b = k
                break
            else:
                y += 1
        k = c[b]
        while(z > 0):
            s[k % 7] = s[k % 7] + 1 
            z -= 1
            k += 1
        for l in s:
            print(l, end=" ")
        print()
