for i in range(int(input())):
    s = int(input())
    c = ['LB','MB','UB','LB','MB','UB','SU','SL']
    j = (s - 1) % 8
    if 0 <= j <= 2:
        print(str(s + 3) + c[j])
    elif 3 <= j <= 5:
        print(str(s - 3) + c[j])
    elif j == 6:
        print(str(s + 1) + c[j])
    else:
        print(str(s - 1) + c[j])
