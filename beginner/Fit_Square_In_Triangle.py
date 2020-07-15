for i in range(int(input())):
    j = int(input())
    j -= 2
    j //= 2
    s = (j * (j + 1)) // 2
    print(s)
