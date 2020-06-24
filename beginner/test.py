x = int(input())
y = int(input())
for i in range(0, y + 1):
    lst = []
    for j in range(0, x + 1):
        lst = lst + [(i,j)]
    print(lst)
