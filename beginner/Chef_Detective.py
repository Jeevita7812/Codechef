s = int(input())
b = set(map(int,input().split()))
for j in range(1,s + 1):
    if j not in b:
        print(j,end = " ")
