n, k = map(int, input().split())
a = list(map(int,input().split()))
p, q = [[a[0],0]],1000000007
for j in range(1,n):
    if(j - p[0][1] > k):
        p.pop(0)
    t = p[0][0] * a[j]
    while(len(p) != 0 and t < p[-1][0]):
        p.pop()
    p.append([t,j])
op = p[-1][0] % q
print(op)
