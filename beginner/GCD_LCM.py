def gcd(x,y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
def compute_lcm(x, y):
        if x > y:
            greater = x
        else:
            greater = y
        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
        return lcm

t = int(input())
for i in range(t):
    n = map(int,input().split())
    n = sorted(n)
    a = int(n[0])
    b = int(n[1])
    GCD = str(gcd(a,b))
    lcm = str(compute_lcm(a,b))
    print(GCD +' ' +  lcm)
