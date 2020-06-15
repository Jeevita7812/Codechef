s = input()
lst1 = []
lst2 = []
t = int(input())
for j in range(len(s)):
    lst1 = lst1 + [j]
for i in range(t):
    n = input()
    for k in range(len(n)):
        lst2 = lst2 + [k]
    o = sorted(lst1)
    p = sorted(lst2)
    if o == p:
        print("Yes")
    else:
        print("No")
