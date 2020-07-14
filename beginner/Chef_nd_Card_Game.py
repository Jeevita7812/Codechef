for i in range(int(input())):
    win_c = 0
    win_m = 0
    draw = 0
    for k in range(int(input())):
        y, z = input().split()
        j = 0
        s = 0
        for c in y:
            j = int(c) + j
        for l in z:
            s = int(l) + s
        if j > s:
            win_c += 1
        elif s > j:
            win_m += 1
        else:
            draw += 1
    if win_c + draw > win_m + draw:
        print("0" + " " + str(win_c + draw))
    elif win_c + draw == win_m + draw:
        print("2" + " " + str(win_m + draw))
    else:
        print("1" + " " + str(win_m + draw))
