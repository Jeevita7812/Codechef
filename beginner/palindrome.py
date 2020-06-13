t = int(input())
for i in range(t):
    n = int(input())
    t = input()
    jlj = ""
    for slj in n:
        jlj = slj + jlj
    jlj = int(jlj)
    if n == jlj:
        print("wins")
    else:
        print("losses")
