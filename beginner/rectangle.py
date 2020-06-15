t = int(input())
for i in range(t):
    n = list(map(int, input().split()))
    n = sorted(n)
    if n[0] == n[1] and n[2] == n[3]:
        print("YES")
    else:
        print("NO")
