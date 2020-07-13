for i in range(int(input())):
    j, s = map(int, input().split())
    yz = -1
    for k in range(1,s + 1):
        if(j % k > yz):
            yz = j % k
    print(yz)
