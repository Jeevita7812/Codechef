for j in range(int(input())):
    n, p = map(int, input().split())
    l = list(map(int, input().split()))
    cakewalk = p // 2
    hard = p // 10
    cakewalk_count = 0
    hard_count = 0
    for i in range(len(l)):
        if l[i] <= hard:
            hard_count += 1
        if l[i] >= cakewalk:
            cakewalk_count += 1
    if hard_count == 2 and cakewalk_count == 1:
        print("yes")
    else:
        print("no")
