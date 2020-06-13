n,k = input().split()
n = int(n)
k = int(k)
count = 0
for _ in range (n):
    t = input()
    t = int(t)
    if t % k == 0:
        count = count + 1
print(count)
