for _ in range(int(input())):
    m,x,y = map(int,input().split())
    l = list(map(int,input().split()))
    mul = x*y
    ans =0
    for i in range(1,101):
        count=0
        for e in l:
            left=e-mul
            right=e+mul
            if(left<0): left=1
            if(right>100): right=100
            if(i>=left and i<=right):
               break
            else: count=count+1
        if(count==m): ans=ans+1
    print(ans)
