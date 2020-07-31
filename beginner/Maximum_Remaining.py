s = int(input())
j = list(set(map(int, input().split())))
if len(j) > 1:
    j.sort()
    print(j[-2])
else:
    print(0)
