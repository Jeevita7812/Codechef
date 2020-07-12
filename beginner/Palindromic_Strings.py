for k in range(int(input())):
    j = input()
    s = input()
    for i in j:
        if i in s:
            print("Yes")
            break
    else:
        print("No")
