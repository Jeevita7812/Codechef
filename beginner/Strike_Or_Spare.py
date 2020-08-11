for i in range(int(input())):
    j = int(input())
    if j % 2 == 0:
        print(1, 10 ** (j // 2))
    else:
        print(1, 10 ** (((j + 1) // 2) - 1))
