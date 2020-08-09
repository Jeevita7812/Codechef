for i in range(int(input())):
    n,m = map(int,input().split())
    count1,count2 =0,0
    for j in range(n):
        s = input()
        if(j%2==0):
            for l in range(m):
                if l%2==0:
                    if s[l]!='R':
                        count1+=3
                    else:
                        count2+=5
                else:
                    if s[l]!='G':
                        count1+=5
                    else:
                        count2+=3
        else:
            for l in range(m):
                if l%2==0:
                    if s[l]!='R':
                        count2+=3
                    else:
                        count1+=5
                else:
                    if s[l]!='G':
                        count2+=5
                    else:
                        count1+=3
    print(min(count1,count2))
