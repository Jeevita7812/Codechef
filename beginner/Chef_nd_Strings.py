for i in range(int(input())):
    s = input()
    l = len(s)
    k = 0
    j = 0
    czy = 0
    p = 'chef'
    p = sorted(p)
    while k <= l - 4:
        st = s[k:k + 4]
        st = sorted(st)
        if st == p:
            j = 1
            czy += 1
        k += 1
    if j == 1:
        print("lovely ",czy)
    else:
        print("normal")
