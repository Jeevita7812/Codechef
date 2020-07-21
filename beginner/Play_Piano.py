for i in range(int(input())):
    j = input()
    s = len(j)
    for c in range(1,s,2):
        if(j[c] == j[c - 1]):
            print("no")
            break
    else:
        print("yes")
