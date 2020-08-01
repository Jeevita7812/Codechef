n = int(input())
j = list(map(int, input().split()))
y = list(map(int, input().split()))
c = 100000
s = 100000
z = 1000000
for i in range(n):
    if(y[i] == 1 and j[i] < s):
        s = j[i]
    elif(y[i] == 2 and j[i] < c):
        c = j[i]
    elif(y[i] == 3 and j[i] < z):
        z = j[i]
print(min(s + c, z))
