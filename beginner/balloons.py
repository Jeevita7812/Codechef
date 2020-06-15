for i in range(int(input())):
    n = input()
    a_count = 0
    b_count = 0
    for j in n:
        if 'a' == j:
            a_count+=1
        else:
            b_count+=1
    if a_count > b_count:
        print(b_count)
    else:
        print(a_count)
