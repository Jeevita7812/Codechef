t = int(input())
for i in range(t):
    n = int(input())
    for jls in range(2,n):
        if n % jls == 0:
            print('no')
            break;
    else:
        print('yes')
